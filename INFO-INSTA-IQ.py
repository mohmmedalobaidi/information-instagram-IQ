import requests
import pyfiglet


# Regular Colors
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
C ='\033[0;36m' # Cyan
W ='\033[0;37m' # White

print("")
print("")
print(B+" #**************************************************************************************************#")
print("")

print(W+"""
██╗███╗   ██╗███████╗ ██████╗     ██╗███╗   ██╗███████╗████████╗ █████╗  ██████╗ ██████╗  █████╗ ███╗   ███╗    
██║████╗  ██║██╔════╝██╔═══██╗    ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██╔════╝ ██╔══██╗██╔══██╗████╗ ████║    
██║██╔██╗ ██║█████╗  ██║   ██║    ██║██╔██╗ ██║███████╗   ██║   ███████║██║  ███╗██████╔╝███████║██╔████╔██║    
██║██║╚██╗██║██╔══╝  ██║   ██║    ██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║   ██║██╔══██╗██╔══██║██║╚██╔╝██║    
██║██║ ╚████║██║     ╚██████╔╝    ██║██║ ╚████║███████║   ██║   ██║  ██║╚██████╔╝██║  ██║██║  ██║██║ ╚═╝ ██║    
╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝     ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝    
""")
print("")
print(Z+"""
                                        BY : Eng Mohammed Al-Obaidy
                                        TELE : @hckiq
                                        GITHUB : @Engmohammedalobaidy
""")


print("")
print(B+" #**************************************************************************************************#")
print("")
username = input(' \033[0;37m [#] \033[0;36mUserName \033[1;33m: ')

url = f'https://www.instagram.com/{username}/?__a=1'
r = requests.get(url).json()
username = r ['graphql']['user']['full_name']
bio = r ['graphql']['user']['biography']
profile_pic = r ['graphql']['user']['profile_pic_url_hd']
posts = r ['graphql']['user']['edge_owner_to_timeline_media']['count']
followers = r ['graphql']['user']['edge_followed_by']['count']
following = r ['graphql']['user']['edge_follow']['count']
print(Z+"-----------------------------------------------------")
print("")
print("")
print("")
print(f' \033[0;37m[#] \033[0;36mUserName \033[1;33m: {username}')
print("")
print(f' \033[0;37m[#] \033[0;36mBio \033[1;33m: {bio}')
print("")
print(f' \033[0;37m[#] \033[0;36mPosts \033[1;33m: {posts}')
print("")
print(f' \033[0;37m[#] \033[0;36mFollowers \033[1;33m: {followers}')
print("")
print(f' \033[0;37m[#] \033[0;36mFollowing \033[1;33m: {following}')
print("")
print(F+"     The image has been saved successfully")
print("")
print("")
print(Z+"-----------------------------------------------------")
pic = requests.get(profile_pic)
with open('profile profile.png','wb') as f :
    f.write(pic.content)
