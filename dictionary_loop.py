tmp = {
    "items": [
        {
            "id": 1
        },
        {
            "id": 2
        },
        {
            "id": 3
        }]
}

for item in tmp:
    for objs in tmp[item]:
        print(objs["id"])
        # print(objs)
        #to trouble-shoot, simply print the loop


# for item in tmp["items"]:
#     print(item["id"])
# another variation of the loop



https://www.dropbox.com/s/tms8uoj8fhyj9n3/Screenshot%202019-09-19%2014.27.02.png?dl=0

ex = [{"test": "tmp", "test1":"tmp1"}, 2]
print(ex[0]["test1"])

exit()
