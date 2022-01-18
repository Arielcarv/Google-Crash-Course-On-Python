#!/usr/bin/env python3

import csv
import re

def contains_domain(address, domain):
    """Returns True if the email address contains the given domain,
    in the domain position, false if not."""
    domain = r'[\w\.-]+@'+domain+'$'
    if re.match(domain, address):
        return True
    return False

def replace_domain(address, old_domain, new_domain):
    """Replaces the old domain with the new domain in
    the received address."""
    old_domain_pattern = r'' + old_domain + '$'
    address = re.sub(old_domain_pattern, new_domain, address)
    return address

def main():
    """Processes the list of emails, replacing any instances of the
    old domain with the new domain."""
    old_domain, new_domain = "abc.edu", "xyz.edu"
    csv_file_location = './user_emails.csv'
    report_file =  './updated_user_emails.csv'

    user_email_list = []
    old_domain_email_list = []
    new_domain_email_list = []

    with open(csv_file_location, 'r') as f:
        user_data_list = list(csv.reader(f))
        print(f"USER DATA LIST: {user_data_list}\n")
        user_email_list = [data[1].strip() for data in user_data_list[1:]]
        print(f"USER EMAIL LIST: {user_email_list}\n")
        for email_address in user_email_list:
            if contains_domain(email_address, old_domain):
                old_domain_email_list.append(email_address)
                replaced_email = replace_domain(email_address, old_domain, new_domain)
                new_domain_email_list.append(replaced_email)
        email_key = ' ' + 'Email Address'
        email_index = user_data_list[0].index(email_key)
        print(f"EMAIL INDEX: {email_index}.\n")

        for user in user_data_list[1:]:
            for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
                if user[email_index] == ' ' + old_domain:
                    user[email_index] = ' ' + new_domain

    print(f"OLD DOMAIN LIST: {old_domain_email_list}\n")
    print(f"NEW DOMAIN LIST: {new_domain_email_list}\n")
    print(f"*NEW* USER DATA LIST: {user_data_list}\n")
    
    f.close()

    with open(report_file, 'w+') as output_file:
        writer = csv.writer(output_file)
        writer.writerows(user_data_list)
        output_file.close()


main()

# USER DATA LIST: [['Full Name', ' Email Address'], ['Blossom Gill', ' blossom@abc.edu'], ['Hayes Delgado', ' nonummy@utnisia.com'], ['Petra Jones', ' ac@abc.edu'], ['Oleg Noel', ' noel@liberomauris.ca'], ['Ahmed Miller', ' ahmed.miller@nequenonquam.co.uk'], ['Macaulay Douglas', ' mdouglas@abc.edu'], ['Aurora Grant', ' enim.non@abc.edu'], ['Madison Mcintosh', ' mcintosh@nisiaenean.net'], ['Montana Powell', ' montanap@semmagna.org'], ['Rogan Robinson', ' rr.robinson@abc.edu'], ['Simon Rivera', ' sri@abc.edu'], ['Benedict Pacheco', ' bpacheco@abc.edu'], ['Maisie Hendrix', ' mai.hendrix@abc.edu'], ['Xaviera Gould', ' xlg@utnisia.net'], ['Oren Rollins', ' oren@semmagna.com'], ['Flavia Santiago', ' flavia@utnisia.net'], ['Jackson Owens', ' jackowens@abc.edu'], ['Britanni Humphrey', ' britanni@ut.net'], ['Kirk Nixon', ' kirknixon@abc.edu'], ['Bree Campbell', ' breee@utnisia.net']]

# USER EMAIL LIST: ['blossom@abc.edu', 'nonummy@utnisia.com', 'ac@abc.edu', 'noel@liberomauris.ca', 'ahmed.miller@nequenonquam.co.uk', 'mdouglas@abc.edu', 'enim.non@abc.edu', 'mcintosh@nisiaenean.net', 'montanap@semmagna.org', 'rr.robinson@abc.edu', 'sri@abc.edu', 'bpacheco@abc.edu', 'mai.hendrix@abc.edu', 'xlg@utnisia.net', 'oren@semmagna.com', 'flavia@utnisia.net', 'jackowens@abc.edu', 'britanni@ut.net', 'kirknixon@abc.edu', 'breee@utnisia.net']

# EMAIL INDEX: 1.

# OLD DOMAIN LIST: ['blossom@abc.edu', 'ac@abc.edu', 'mdouglas@abc.edu', 'enim.non@abc.edu', 'rr.robinson@abc.edu', 'sri@abc.edu', 'bpacheco@abc.edu', 'mai.hendrix@abc.edu', 'jackowens@abc.edu', 'kirknixon@abc.edu']

# NEW DOMAIN LIST: ['blossom@xyz.edu', 'ac@xyz.edu', 'mdouglas@xyz.edu', 'enim.non@xyz.edu', 'rr.robinson@xyz.edu', 'sri@xyz.edu', 'bpacheco@xyz.edu', 'mai.hendrix@xyz.edu', 'jackowens@xyz.edu', 'kirknixon@xyz.edu']

# *NEW* USER DATA LIST: [['Full Name', ' Email Address'], ['Blossom Gill', ' blossom@xyz.edu'], ['Hayes Delgado', ' nonummy@utnisia.com'], ['Petra Jones', ' ac@xyz.edu'], ['Oleg Noel', ' noel@liberomauris.ca'], ['Ahmed Miller', ' ahmed.miller@nequenonquam.co.uk'], ['Macaulay Douglas', ' mdouglas@xyz.edu'], ['Aurora Grant', ' enim.non@xyz.edu'], ['Madison Mcintosh', ' mcintosh@nisiaenean.net'], ['Montana Powell', ' montanap@semmagna.org'], ['Rogan Robinson', ' rr.robinson@xyz.edu'], ['Simon Rivera', ' sri@xyz.edu'], ['Benedict Pacheco', ' bpacheco@xyz.edu'], ['Maisie Hendrix', ' mai.hendrix@xyz.edu'], ['Xaviera Gould', ' xlg@utnisia.net'], ['Oren Rollins', ' oren@semmagna.com'], ['Flavia Santiago', ' flavia@utnisia.net'], ['Jackson Owens', ' jackowens@xyz.edu'], ['Britanni Humphrey', ' britanni@ut.net'], ['Kirk Nixon', ' kirknixon@xyz.edu'], ['Bree Campbell', ' breee@utnisia.net']]