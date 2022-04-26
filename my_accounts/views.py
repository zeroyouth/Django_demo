from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def sign_up(request):

    # 요청이 post인지 확인
    context = {}
    if request.method == 'POST':
    # 1. 요청받은 request에서 username 존재하는지
    # 2. 요청받은 request에서 password가 존재하는지
    # 3. 요청받은 request에서 password와 password_check가 같은지

        username = request.POST.get('username')
        password = request.POST.get('password')
        password_check = request.POST.get('password_check')
        if (username and password and password == password == password_check):
            try:
              new_user = User.objects.create_user(username=username, password=password)
              auth.login(request, new_user)
              return HttpResponseRedirect(reverse('blog:home'))

            except:
              context['error'] = '이미 존재하는 아이디입니다.'
    # 회원가입 ok 
    # 새로운 유저 아이디로로그인
    # 블로그 홈으로 리다이렉트 시켜주기
    else:
        context['error'] = '아이디와 비밀번호를 잘못 입력하셨습니다.'
    # 에러메시지 context에 담기

    return render(request, 'my_accounts/sign_up.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('blog:home')
    context={}
    # 요청이 post인지 확인
    if request.method == 'POST':

    # 아이디 O
      username = request.POST.get('username')
    # 비밀번호 O
      password = request.POST.get('password')
      if (username and password):
          # 비밀번호 체크 -----추가적으로 필요한 함수
          user = auth.authenticate(request, username=username, password=password)
          # 로그인 O
          if user:
              auth.login(request, user)
              # 리다이렉트 O 
              return redirect('blog:home')
          else:
              context['error'] = '아이디랑 비밀번호 틀렸습니다...'
      else:
        context['error'] = '아이디 혹은 비밀번호를 입력해주세요..!'
    # context에 에러메시지 담아주기
      return render(request, 'my_accounts/login.html',context)

def logout(request):
    # 요청이 post인지 확인!
    if request.method == "POST":
        auth.logout(request)
      # 로그아웃 O

    # 리다이랙트 O
    return redirect('blog:home')