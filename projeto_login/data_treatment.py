def txt_creating():
    # Caso arquivo não exista, criá-lo:
    try:
        archive_treat = open('users_data.txt', 'r+')
        archive_treat.close()
    except FileNotFoundError:
        archive_treat = open('users_data.txt', 'a+')
        archive_treat.close()


def data_to_txt(email, password):
    # Escrevendo
    try:
        archive_treat = open('users_data.txt', 'a')
    except Exception:
        print('Error opening the database.')
    else:
        try:
            archive_treat.write(f'{email} {password}\n')
        except Exception:
            print('Error in the data passing.')
        else:
            archive_treat.close()
