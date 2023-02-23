#html process checker

with open("homepage.html.txt") as f:
    lines = f.readlines()
    data= []
    head= []
    body=[]
    head_bool=False
    body_bool= False
    #split up body and head of html document
    for line in lines:
        if len(line.split())!= 0:
            if "<head>" in line.split()[0] or "</head>" in line.split()[0]:
                if "<head>" in line.split()[0]:
                    head_bool= True
                else:
                    head_bool= False
                    head.append(line)
            if "<body" in line.split()[0] or "</body>" in line.split()[0]:
                if "<body" in line.split()[0]:
                    body_bool= True
                else:
                    body_bool= False
                    body.append(line)

            if head_bool:
                head.append(line)
            if body_bool:
                body.append(line)


    def process_div(html):
        div_bool=False
        div_open_count=0
        div_close_count=0
        div_data=[]
        temp=[]
        #Split up <div containers of the body
        for line in html:
            if "<div" in line.split()[0]:
                div_bool=True
                div_open_count+=1
                if div_open_count==1:
                    continue

            if "</div>" in line.split()[0]:
                div_close_count+=1
                if div_close_count==div_open_count:
                    div_bool=False
                    div_open_count=0
                    div_close_count=0
                    div_data.append(temp)
                    temp=[]

            if div_bool:
                temp.append(line)

        return div_data

    #created a data structure that helps process the different divs and breaks them down
    q=[body]
    final_data=[]
    while len(q)>0:
        div=q.pop(0)
        div_data=process_div(div)
        if div_data:
            for d in div_data:
                q.append(d)
        final_data.append(div)

    for data in final_data:
        print (data)
