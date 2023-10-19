### 3. Linode

- This "SSH_Configuration" role configures SSH to disable password-based authentication and enable pubkey authentication.

```yaml
- name: Disable password-based authentication in SSH
  lineinfile:
    dest: /etc/ssh/sshd_config
    regexp: '^PasswordAuthentication'
    line: 'PasswordAuthentication no'
    state: present
  notify:
    - Reload SSH

- name: Ensure PubkeyAuthentication is enabled
  lineinfile:
    dest: /etc/ssh/sshd_config
    regexp: '^PubkeyAuthentication'
    line: 'PubkeyAuthentication yes'
    state: present
  notify:
    - Reload SSH
```

- This task creates Linode instances based on the defined configuration in the firewall_instances variable. It loops through three categories: 'db', 'queue', and 'controller'.
```yaml
- name: Create Linode Instances
  linode.cloud.instance:
    api_token: "{{ api_token }}"
    label: "my-linode-{{ item.name }}"
    type: "{{ plan }}"
    region: "{{ region }}"
    image: "{{ image }}"
    authorized_keys:
      - "{{ lookup('file', authorized_keys_file) }}"
    wait: yes
    wait_timeout: 600
    private_ip: yes
    tags:
      - env=prod
    state: present
  loop: "{{ firewall_instances['db'] + firewall_instances['queue'] + firewall_instances['controller'] }}"
  register: linode_instances
```

- Collects information about the created Linode instances, including their process IDs and IP addresses.
```yaml
- name: Get Linode Instance Info
  linode.cloud.instance_info:
    api_token: "{{ api_token }}"
    label: "my-linode-{{ item.name }}"
  loop: "{{ firewall_instances['db'] + firewall_instances['queue'] + firewall_instances['controller'] }}"
  register: linode_instance_info
```
- This "DB_Firewall" role sets up firewall rules for the database VM.
```yaml
- name: Create Firewall DB
  linode.cloud.firewall:
    api_token: "{{ api_token }}"
    label: "DB-firewall"
    rules:
      inbound_policy: DROP
      inbound:
        - action: ACCEPT
          label: allow-ping
          addresses:
            ipv4:
              - "0.0.0.0/0" # Allow all IPv4 addresses
            ipv6:
              - "::/0" # Allow all IPv6 addresses
          description: Allow ICMP (ping) traffic
          protocol: ICMP # Allow ICMP traffic
        - action: ACCEPT
          label: allow-private-in
          addresses:
            ipv4:
              - "0.0.0.0/0" # Allow all IPv4 addresses
            ipv6:
              - "::/0" # Allow all IPv6 addresses
          description: Allow inbound traffic from private IPs.
          ports: "22,3306" # Allow all ports
          protocol: TCP # Allow both TCP and UDP
      outbound_policy: DROP
      outbound:
        - action: ACCEPT
          label: allow-ping
          addresses:
            ipv4:
              - "0.0.0.0/0" # Allow all IPv4 addresses
            ipv6:
              - "::/0" # Allow all IPv6 addresses
          description: Allow ICMP (ping) traffic
          protocol: ICMP # Allow ICMP traffic
        - action: ACCEPT
          label: allow-private-out
          addresses:
            ipv4:
              - "0.0.0.0/0" # Allow all IPv4 addresses
            ipv6:
              - "::/0" # Allow all IPv6 addresses
          description: Allow outbound traffic from private IPs.
          ports: "22,3306" # Allow all ports
          protocol: TCP # Allow both TCP and UDP
    state: present
register: firewall_db
```
- This "DB_Controller" role sets up firewall rules for the controller VM.
```yaml
- name: Create Firewall Controller
  linode.cloud.firewall:
    api_token: "{{ api_token }}"
    label: "CN-firewall"
    rules:
      inbound_policy: DROP
      inbound:
        - action: ACCEPT
          label: allow-ping
          addresses:
            ipv4:
              - "0.0.0.0/0" # Allow all IPv4 addresses
            ipv6:
              - "::/0" # Allow all IPv6 addresses
          description: Allow ICMP (ping) traffic
          protocol: ICMP # Allow ICMP traffic
        - action: ACCEPT
          label: allow-private-in
          addresses:
            ipv4:
              - "0.0.0.0/0" # Allow all IPv4 addresses
            ipv6:
              - "::/0" # Allow all IPv6 addresses
          description: Allow inbound traffic from private IPs.
          ports: "443,80,53,853,22" # Allow all ports
          protocol: TCP # Allow both TCP and UDP
      outbound_policy: DROP
      outbound:
        - action: ACCEPT
          label: allow-ping
          addresses:
            ipv4:
              - "0.0.0.0/0" # Allow all IPv4 addresses
            ipv6:
              - "::/0" # Allow all IPv6 addresses
          description: Allow ICMP (ping) traffic
          protocol: ICMP # Allow ICMP traffic
        - action: ACCEPT
          label: allow-private-out
          addresses:
            ipv4:
              - "0.0.0.0/0" # Allow all IPv4 addresses
            ipv6:
              - "::/0" # Allow all IPv6 addresses
          description: Allow outbound traffic from private IPs.
          ports: "443,80,53,853,22" # Allow all ports
          protocol: TCP # Allow both TCP and UDP
    state: present
register: firewall_cntrl
```
- This "Queue_Firewall" role sets up firewall rules for the Queue (RabbitMQ) VM.
```yaml
- name: Create Firewall Queue
  linode.cloud.firewall:
    api_token: "{{ api_token }}"
    label: "QU-firewall"
    rules:
      inbound_policy: DROP
      inbound:
        - label: allow-private-in
          addresses:
            ipv4:
              - "10.0.0.0/8" # Private IP address range
          description: Allow inbound traffic from private IPs.
          ports: "15672,5672" # Allow all ports
          protocol: TCP # Allow both TCP and UDP
          action: ACCEPT
      outbound_policy: DROP
      outbound:
        - action: ACCEPT
          label: allow-private-out
          addresses:
            ipv4:
              - "10.0.0.0/8" # Private IP address range
          description: Allow outbound traffic from private IPs.
          ports: "15672,5672" # Allow all ports
          protocol: TCP # Allow both TCP and UDP
    state: present
register: firewall_queue
```

- This "Attach_InstanceDB" role attaches the created instances to the Database Firewall.
```yaml
- name: Attach instances to DB Firewall
  linode.cloud.firewall_device:
    api_token: "{{ api_token }}"
    firewall_id: "{{ firewall_db.firewall.id }}"
    entity_id: "{{ linode_instances.results | selectattr('item.name', 'eq', item.name) | map(attribute='instance.id') | list | first }}"
    entity_type: "linode"
    state: present
  loop: "{{ firewall_instances['db'] }}"
```
- This "Attach_InstanceQueue" role attaches the created instances to the Queue Firewall.
```yaml
- name: Attach instances to Queue Firewall
  linode.cloud.firewall_device:
    api_token: "{{ api_token }}"
    firewall_id: "{{ firewall_queue.firewall.id }}"
    entity_id: "{{ linode_instances.results | selectattr('item.name', 'eq', item.name) | map(attribute='instance.id') | list | first }}"
    entity_type: "linode"
    state: present
  loop: "{{ firewall_instances['queue'] }}"
```
- This "Attach_InstanceController" role attaches the created instances to the Controller Firewall.
```yaml
- name: Attach instance to Controller Firewall
  linode.cloud.firewall_device:
    api_token: "{{ api_token }}"
    firewall_id: "{{ firewall_cntrl.firewall.id }}"
    entity_id: "{{ linode_instances.results | selectattr('item.name', 'eq', item.name) | map(attribute='instance.id') | list | first }}"
    entity_type: "linode"
    state: present
  loop: "{{ firewall_instances['controller'] }}"
```
