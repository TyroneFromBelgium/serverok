### 3. Linode
#### 3.1 Main playbook & Variables:
- These are the variables that are being used inside the playbook.
    - api_token = You can generate your own Linode API key on the Linode website.
    - region = The region you want to host your VM's on.
    - plan = You can view all the available plans on Linode website to find out which one is most suitable for your needs.
    - image = Defining the image for the Linode instances.
    - authorized_keys_file = Here, you provide the path to your SSH public key.
    - firewall_instances = This variable defines the configuration for the instances. You can specify the names of instances in each category.
```yaml
vars:
    api_token: "186f959d24f2011b4b762094fce1e32140eb80cd8e696227d00b63bd0daabc6d"
    region: eu-central
    plan: g6-standard-2
    image: linode/rocky9
    authorized_keys_file: "/home/ael/.ssh/id_rsa.pub"
    firewall_instances:
      db:
        - name: "db1"
        - name: "db2"
      queue:
        - name: "qu1"
      controller:
        - name: "cont1"
roles:
    - name: SSH_Configuration
      role: roles/SSH_Configuration
    - name: CreateLinodeInstances
      role: roles/CreateLinodeInstances
    - name: LinodeInstanceInfo
      role: roles/LinodeInstanceInfo
    - name: HostFileRole
      role: roles/HostFileRole
    - name: DatabaseFirewall
      role: roles/DatabaseFirewall
    - name: ControllerFirewall
      role: roles/ControllerFirewall
    - name: QueueFirewall
      role: roles/QueueFirewall
    - name: Attach_DatabaseFirewall
      role: roles/Attach_DatabaseFirewall
    - name: Attach_ControllerFirewall
      role: roles/Attach_ControllerFirewall
    - name: Attach_QueueFirewall
      role: roles/Attach_QueueFirewall
```

--------------------------------------------------------------
#### 3.2 Tasks/Roles:
- This "SSH_Configuration" role configures SSH to disable password-based authentication and enable pubkey authentication.x²
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

- This "CreateLinodeInstances" role creates Linode instances based on the defined configuration in the firewall_instances variable. It loops through three categories: 'DB', 'Queue', and 'Controller'.
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
- This "LinodeInstanceInfo" role gathers information about the created Linode instances, including their process IDs and IP addresses
```yaml
- name: Get Linode Instance Info
  linode.cloud.instance_info:
    api_token: "{{ api_token }}"
    label: "my-linode-{{ item.name }}"
  loop: "{{ firewall_instances['db'] + firewall_instances['queue'] + firewall_instances['controller'] }}"
  register: linode_instance_info
```
- This "DB_Firewall" role sets up firewall rules for the Database VM.
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
- This "Controller_Firewall" role sets up firewall rules for the Controller VM.
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
- This "HostFileRole" role generates an inventory file named "hosts" using a Jinja2 template ("inventory_template.ini.j2") and then displays the results.
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
- This Ansible inventory file template organizes Linode instances into groups (controller, db, queue, dnsmaster, dnsslave) based on their labels, associating each instance's label and public IPv4 address with the respective group.
```jinja
[controller]
{% for instance in linode_instance_info.results %}
{% if 'cont' in instance.instance.label %}
{{ instance.instance.label }} ansible_host= {{ instance.networking.ipv4.public[0].address}}
{% endif %}
{% endfor %}

[db]
{% for instance in linode_instances.results %}
{% if 'db' in instance.instance.label %}
{{ instance.instance.label }} ansible_host= {{ instance.networking.ipv4.public[0].address}}
{% endif %}
{% endfor %}

[queue]
{% for instance in linode_instances.results %}
{% if 'qu' in instance.instance.label %}
{{ instance.instance.label }} ansible_host= {{ instance.networking.ipv4.public[0].address}}
{% endif %}
{% endfor %}

[dnsmaster]
{% for instance in linode_instances.results %}
{% if 'dnsmaster' in instance.instance.label %}
{{ instance.instance.label }} ansible_host= {{ instance.networking.ipv4.public[0].address}}
{% endif %}
{% endfor %}

[dnsslave]
{% for instance in linode_instances.results %}
{% if 'dnsslave' in instance.instance.label %}
{{ instance.instance.label }} ansible_host= {{ instance.networking.ipv4.public[0].address}}
{% endif %}
{% endfor %}
```
