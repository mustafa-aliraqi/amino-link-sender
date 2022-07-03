import samino
client=samino.Client()
client.login("email", "password")
comids=client.get_my_communitys().comId
while True:
    a=str(input("enter a community link or chat link: "))
    aa=client.get_from_link(a).comId
    client.join_community(aa)
    print("done ....\ndo you want to join another comunity?")
    aaa=str(input("type(y/n): "))
    if aaa=="n":
        break
    else:
        pass
a=str(input("type text to send: "))
for comid in comids:
    users=samino.Local(comid).get_online_users(size=1000).userId
    for user in users:
        try:
            samino.Local(comid).start_chat(user,"اعلان مهم جدا",a)
        except:
            pass
        
