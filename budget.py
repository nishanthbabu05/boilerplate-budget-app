class Category:



    def __init__(self, cat, ledger=None, bal=0.0,x="",t=""):
        if ledger is None:
            ledger = []
        self.cat = cat
        self.ledger = ledger
        self.bal = bal
        self.x=self.cat.center(30,"*")+"\n"
        self.t=t



    def deposit(self, amt, des=""):
        self.ledger.append({"amount": amt, "description": des})
        self.bal += amt

    def withdraw(self, amt, des=""):
        if self.check_funds(amt):
            self.ledger.append({"amount": -amt, "description": des})
            self.bal -= amt
            return True
        else:
            return False

    def get_balance(self):
        return self.bal

    def transfer(self, amt, ob):
        if self.check_funds(amt):
            self.withdraw(amt, "Transfer to " + ob.cat)
            ob.deposit(amt, "Transfer from " + self.cat)
            
            return True
        else:
            return False

    def check_funds(self, amt):
        if (amt > self.bal):
            return False
        else:
            return True

    def __str__(self):

      for i in self.ledger:
        self.t=self.t+i["description"][:23]+"{:0.2f}".format(round(float(i["amount"]),2)).rjust(30-len(i["description"][:23]))+"\n"
      return self.x+self.t+"Total: {:0.2f}".format(self.bal)
def create_spend_chart(categories):
    tt=0
    p1=[]

    for i in categories:
        for k in i.ledger:
            if(k["amount"]<0):
                tt+=abs(k["amount"])
    for j in categories:
        pr=0
        for e in j.ledger:
            if(e["amount"]<0):
                pr=pr+(-1*e["amount"])


        pr/=tt



        pr=round(pr*10)*10


        if pr==10:
            pr=0

        p1.append(pr)
    rr=""



    if(len(categories)<4):
        n=100

        rr=rr+"Percentage spent by category\n"
        while(n>=0):
            c = 0
            ll=str(n).rjust(3)+"|"
            for p in p1:

                if p>=n:

                    if(c==0):
                        ll=ll+" o"
                        c+=1
                    elif (p1[len(p1) - 1] == p):
                        ll = ll + "  o  "
                    else:
                        ll=ll+"  o"
                else:
                    if (c == 0):
                        ll = ll + "  "
                        c += 1
                    elif(p1[len(p1)-1]==p):
                        ll = ll + "     "
                    else:
                        ll = ll + "   "

            rr=rr+ll+"\n"
            n-=10

        q="---"*len(categories)+"-"
        rr=rr+q.rjust(4+len(q))+"\n"
        maxlen=0
        for i in categories:
            if(len(i.cat)>maxlen):
                maxlen=len(i.cat)
        f=0

        while(maxlen>0):
            cc = 0
            for i in categories:
                if i.cat[f:f+1].isalnum():
                    if(cc==0):
                        rr=rr+i.cat[f].rjust(6)+"  "
                        
                        cc += 1
                    else:
                        rr=rr+i.cat[f]+"  "
                        
                else:
                    if (cc == 0):
                        rr=rr+" ".rjust(6)+"  "

                        
                        cc += 1
                    else:
                        rr=rr+" "+"  "
                        

            f+=1
            if (maxlen != 1):
                rr=rr+"\n"
            maxlen-=1
    return rr

  

        
    
