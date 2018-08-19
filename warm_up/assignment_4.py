def group_users_by_email_domain(users):
    new_dict={}
    for each_user in users:
        email_key=each_user['email'][each_user['email'].index("@")+1:len(each_user['email'])]
        new_dict.setdefault(email_key,[])
        new_dict[email_key].append(each_user)
    return new_dict
