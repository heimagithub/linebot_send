from linebot import LineBotApi
from linebot.models import TextSendMessage

# put Channel access token
line_bot_api = LineBotApi('Channel access token')

for i in range(1,1001) :
	str1 = str(i) 	
	# Your user ID 
	line_bot_api.push_message('Your user ID', TextSendMessage(text=str1))

