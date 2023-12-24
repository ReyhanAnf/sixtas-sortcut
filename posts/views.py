from django.shortcuts import render
from .models import Posts, Answers, Replies
from users.views import get_data_user_person

# Create your views here.
def posts_data():
  posts = Posts.objects.all()
  
  all_content = []
  ##################################### Bagian Posts #################################
  for post in posts:
    
    post_dict = {}
    for field in post._meta.get_fields():
      post_dict[field.name] = post.__dict__.get(field.name)
    
    ###################################### Bagian Answer #################################
    
    answers =  Answers.objects.filter(post_id=post_dict['post_id'])
    answers_list = []
    for answer in answers:
      answer_dict = {}
      for field in answer._meta.get_fields():
        answer_dict[field.name] = answer.__dict__.get(field.name)
        
      answer_dict["user_answer"] = get_data_user_person(answer_dict["answerer_id"])[0]
      answers_list.append(answer_dict)
      
      ####################################### Bagian reply ########################################
      
      replies = Replies.objects.filter(answer_id=answer_dict['answer_id'])
      reply_list = []
      for reply in replies:
        reply_dict = {}
        for field in reply._meta.get_fields():
          reply_dict[field.name] = reply.__dict__.get(field.name)
        
        reply_dict["user_reply"] = get_data_user_person(reply_dict["replier_id"])[0]
        reply_list.append(reply_dict)
        
        ##################################### Akhir Reply  #################################
      
      answer_dict["replies"] = reply_list
      
    post_dict["answers"] = answers_list
    post_dict["user_author"] = get_data_user_person(post_dict["author_id"])[0]
    
    all_content.append(post_dict)
    
  return all_content