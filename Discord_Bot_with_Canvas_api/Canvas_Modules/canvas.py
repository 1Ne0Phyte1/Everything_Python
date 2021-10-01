import requests
import os
import shutil

def make_url(uri, api_token, course_id):
    course_url = f"{uri}/courses/?access_token={api_token}"
    files_url = f"{uri}/courses/{course_id}/files?access_token={api_token}"
    if course_id == False:
        return (course_url)
    else:
        return (files_url)


def get_courses(uri, api_token):
    url = make_url(uri, api_token, course_id=False)
    # print(url)

    r = requests.get(url).json()
    t = []
    for i in range(len(r)):
        y = r[i]['id'], r[i]['name']
        t.append(y)
    return t

    # y_n = input("would you like to continue accessing the url? ")
    # if y_n == 'y':
    #     course_id_list = []
    #     ci = ''
    #     while ci != 'q':
    #         ci = (input("Enter course id or 'q' to complete selection: "))
    #         course_id_list.append(ci)
    #     course_id_list = course_id_list[:-1]
    #     courses = [int(x) for x in course_id_list]
    #     for i in courses:
    #         mu = make_url(uri,api_token,i)
    #         get_files(mu)
    # else:
    #     return 0


def get_files(url):

    check = requests.get(url)
    if check.ok == True:
        print(f"The like status is {check.ok}\n")
    else:
        print("The link is down, please give a valid link")

    # Getting the json file
    r = requests.get(url).json()

    # PrettyPrinter for viewing the contents

    print(f'{len(r)} file/s are available for download\n')

    # displaying all the files
    for i in range(len(r)):
        name = r[i]['filename']
        print(i, name)
    print("\n")

    # Creating choice for the user
    choice = int(input("Choose '1' to download files in order\n"
                       "Choose '2' to download specific files\n"))

    # choice '1'
    if choice == 1:
        n = int(
            input("Enter number of files you want to download (enter '0' or a number greater then the number of file"
                  ", to download all files): "))
        if n == 0 or n > len(r):
            n = len(r)
        else:
            pass
        os.mkdir("Files")

        for i in range(n):
            # specifing the files
            file = r[i]['url']
            name = r[i]['filename']
            # print(file, name)


            # extracting the downlod link
            download_link = requests.get(file)

            # Writing the content in to the file
            open(f"Files/{name}", 'wb').write(download_link.content)

        shutil.make_archive("Files", 'zip', "Files")
        shutil.rmtree("Files")



    # choice '2'
    elif choice == 2:
        list = []
        nl = ''
        while nl != 'q':
            nl = (input("Enter file id and 'q' to complete selection:: "))
            list.append(nl)
        list = (list[:-1])

        print(list)

        for i in list:
            if int(i) < len(r):
                # specifing the files
                file = r[int(i)]['url']
                name = r[int(i)]['filename']
                print(name)

                # extracting the downlod link
                download_link = requests.get(file)

                # Writing the content in to the file
                open(f"{name}", 'wb').write(download_link.content)
            else:
                pass
    else:
        print("Invalid choice")
