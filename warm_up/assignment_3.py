def transform_multiple_users_to_dicts(multiple_users):
    users_as_dict=[]
    for i in multiple_users:
        new_dict={
            'name':i[0],
            'email':i[1],
            'age':i[2]
        }
        users_as_dict.append(new_dict)
    return users_as_dict
