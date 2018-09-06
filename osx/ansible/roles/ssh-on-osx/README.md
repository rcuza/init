# Setting Up SSH on OSX

This role will make new keys if they don't exist. It will also manage
the config file.

# Notes

How to get ssh-agent working smoothly?

```
  # - name: install taps with homebrew
  #   homebrew:
  #     name: "{{ item }}"
  #     state: present
  #   with_items:
  #     - openssh

  #- name: install launchagent for ssh-agent
  #  template:
  #    src: org.homebrew.ssh-agent.plist.j2
  #    dest: "{{ ansible_env.HOME }}/Library/LaunchAgents/org.homebrew.ssh-agent.plist"
  #    mode: 0644

  #- name: launchctl load homebrew-ssh-agent
  #  command: "launchctl load {{ ansible_env.HOME }}/Library/LaunchAgents/org.homebrew.ssh-agent.plist"

  #- name: launchctl stop ssh-agent
  #  command: "launchctl stop org.openbsd.ssh-agent"
  #  ignore_errors: yes
```
