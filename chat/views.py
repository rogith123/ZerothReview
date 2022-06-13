from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .utils import get_turn_info
import ipfshttpclient
from dr.models import Doc_upload
# Create your views here.

def peer1(request):
    # get numb turn info
    context = get_turn_info()

    return render(request, 'chat/peer1.html', context=context)

def peer2(request):
    # get numb turn info
    context = get_turn_info()

    return render(request, 'chat/peer2.html', context=context)

def peer(request,apno,pat_name,doc_name):
    # get numb turn info
    context = get_turn_info()
    print('context: ', context)

    return render(request, 'chat/peer.html',{"context":context,"pat_name":pat_name,"doc_name":doc_name,"apno":apno})

def fileUpload(request,apno,doc_name,pat_name):
    if request.method=='POST':
        docx = request.FILES['document']
        # client = ipfshttpclient.connect('/dns/localhost/tcp/8000/http')  # Connects to: /dns/localhost/tcp/5001/http
        # res = client.add(docx)
        # print(res)
        Doc_upload.objects.create(app_id=apno,pat_name = pat_name,doc_name=doc_name,document=docx)
        return render(request,'chat/peer.html',{'msg':'file uploaded','usr':doc_name,'apno':apno,'doc_name':doc_name,'pat_name':pat_name})



# >>> import ipfshttpclient
# >>> client = ipfshttpclient.connect()  # Connects to: /dns/localhost/tcp/5001/http
# >>> res = client.add('test.txt')
# >>> res
# {'Hash': 'QmWxS5aNTFEc9XbMX1ASvLET1zrqEaTssqt33rVZQCQb22', 'Name': 'test.txt'}
# >>> client.cat(res['Hash'])
# 'fdsafkljdskafjaksdjf\n'