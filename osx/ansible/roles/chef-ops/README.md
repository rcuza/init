Role Name
=========

Role for configuing OSX to use chef for operations.

- chefdk
- create `~/.chef/` dir
- create `~/.chef/knife.rb` template

Requirements
------------

N/A

Role Variables
--------------

Uses env variables of user that it is run as.

Dependencies
------------

N/A

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: chef-ops }

License
-------

BSD

Author Information
------------------

An optional section for the role authors to include contact information, or a website (HTML is not allowed).
