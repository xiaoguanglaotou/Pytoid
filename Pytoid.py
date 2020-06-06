import easygui as ezg
file_name = 'Level.json'
ezg.msgbox(msg="欢迎使用Pytoid，一个方便谱师的小程序！",title="Pytoid",ok_button="Level.json编写软件")

def ask_for_basic():
    global file_id
    global file_title
    global file_artist
    global file_illustrator
    global file_charter
    global music_name
    global music_preview
    global background
    file_id = "\"" + ezg.enterbox(msg="请输入铺面ID（关卡唯一的标识符，必须仅由 a~z、0~9、. 和 _ 组成）",title="Pytoid") + "\""
    file_title = "\"" + ezg.enterbox(msg="请输入关卡标题",title="Pytoid") + "\""
    file_artist = "\"" + ezg.enterbox(msg="请输入曲师名称",title="Pytoid") + "\""
    file_illustrator = "\"" + ezg.enterbox(msg="请输入画师名称",title="Pytoid") + "\""
    file_charter = "\"" + ezg.enterbox(msg="请输入谱师名称",title="Pytoid") + "\""
    music_name = "\"" + ezg.enterbox(msg="请输入歌曲文件名称（例如pytoid.mp3，支持.mp3/.ogg/.wav文件）",title="Pytoid") + "\""
    music_preview = "\"" + ezg.enterbox(msg="请输入试听歌曲文件名称",title="Pytoid") + "\""
    background = "\"" + ezg.enterbox(msg="请输入背景文件名称（支持.jpg/.png文件）",title="Pytoid") + "\""

def write_into():
    with open(file_name, 'w') as file_object:
        file_object.write("""{}
      
      \"version\": 1,
      
      \"id\": {},
      \"title\": {},
      \"artist\": {},
      \"illustrator\": {},
      \"charter\": {},
      
      \"music\": {}
        "path\": {}
      {},
      \"music_preview\": {}
        "path": {}
      {},
      \"background\": {}
        \"path\": {}
      {},
      "charts": [""".format("{",file_id,file_title,file_artist,file_illustrator,file_charter,"{",music_name,"}","{",music_preview,"}","{",background,"}"))

def ask_for_times():
    global times
    times = ezg.integerbox(msg="请输入需要多少个铺面（最高三个）",title="Pytoid",lowerbound=1,upperbound=3)
    times = times - 1

def write_charts():
    for i in range(times):
        hard = "\"" + ezg.enterbox(msg="请输入铺面名称",title="Pytoid") + "\""
        difficulty = "\"" + ezg.enterbox(msg="请输入铺面等级",title="Pytoid") + "\""
        file_charts = "\"" + ezg.enterbox(msg="请输入铺面文件名（如pytoid.easy.txt)",title="Pytoid") + "\""
        with open(file_name, 'a') as file_object:
            file_object.write("""
        {}
          \"type\": {}
          \"difficulty\": {}
          \"path\": {}
        {},""".format("{",hard,difficulty,file_charts,"}"))

def write_final_charts():
    hard = "\"" + ezg.enterbox(msg="请输入铺面名称",title="Pytoid") + "\""
    difficulty = "\"" + ezg.enterbox(msg="请输入铺面等级",title="Pytoid") + "\""
    file_charts = "\"" + ezg.enterbox(msg="请输入铺面文件名（如pytoid.easy.txt)",title="Pytoid") + "\""
    with open(file_name, 'a') as file_object:
        file_object.write("""
        {}
          \"type\": {}
          \"difficulty\": {}
          \"path\": {}
        {}
       {}
      ]

{}""".format("{",hard,difficulty,file_charts,"}","}","}"))

ask_for_basic()
write_into()
ask_for_times()
if times == 0:
    write_final_charts()
else:
    write_charts()
    write_final_charts()
    


