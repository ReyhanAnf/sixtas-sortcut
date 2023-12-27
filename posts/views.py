from django.shortcuts import render, redirect
from .models import Posts, Answers, Replies
from users.views import get_data_user_person
from .forms import FormPost, FormAnswer, FormReply

# Create your views here.
def posts_data(users="all"):
  if users == "all":
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
        answer_dict["count"] = len(reply_list)
        answer_dict["vote"] = answer_dict["up"] - answer_dict["down"]
        
      post_dict["answers"] = answers_list
      post_dict["user_author"] = get_data_user_person(post_dict["author_id"])[0]


      post_dict["count"] = len(answers_list)
      
      all_content.append(post_dict)
    
    return all_content
  
  elif type(users) != type('string'):
    print(type(users))
    auth_user = users.user.username
    posts = Posts.objects.filter(author_id=auth_user)
    
    auth_content = []
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
        answer_dict["count"] = len(reply_list)
        answer_dict["vote"] = answer_dict.up - answer_dict.down
        
        
      post_dict["answers"] = answers_list
      post_dict["user_author"] = get_data_user_person(post_dict["author_id"])[0]

      post_dict["count"] = len(answers_list)
      
      auth_content.append(post_dict)
    
    return auth_content
  
  else:
    onepost = users
    posts = Posts.objects.filter(post_id=onepost)
    
    onepost = []
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
        answer_dict["count"] = len(reply_list)
        answer_dict["vote"] = answer_dict.up - answer_dict.down 
        
      post_dict["answers"] = answers_list
      post_dict["user_author"] = get_data_user_person(post_dict["author_id"])[0]
      
      post_dict["count"] = len(answers_list)

      onepost.append(post_dict)
    
    return onepost



# Posting PAGE
def posting(request):
  postData = posts_data(request)
  
  return render(request, 'post/posting.html', {'cposts': postData})

def create_post(request):
  if request.method == 'POST':
    author_id = request.user.username
    content_post = request.POST["content_post"]
    image_post = '' #request.POST["image_post"]
    
    Posts.objects.create(author_id=author_id, content_post=content_post, image=image_post)
    return redirect('../')
  return render(request, 'post/create.html', {'formPost': FormPost})


def create_answer(request, postId):
  postEmbed = posts_data(postId)[0]
  if request.method == 'POST':
    post_id = postId
    answerer_id = request.user.username
    content_answer = request.POST["content_answer"]
    
    
    Answers.objects.create(post_id=post_id, answerer_id=answerer_id, content_answer=content_answer)
    return redirect('../../')
  return render(request, 'post/answer.html', {'formAnswer': FormAnswer, 'postEmbed': postEmbed})


def create_reply(request, answerId):
  answerEmbed = ''
  if request.method == 'POST':
    answer_id = answerId
    replier_id = request.user.username
    content_reply = request.POST["content_reply"]
    
    
    Replies.objects.create(answer_id=answer_id, replier_id=replier_id, content_reply=content_reply)
    return redirect('../../')
  return render(request, 'post/reply.html', {'formReply': FormReply, 'answerEmbed': answerEmbed})
