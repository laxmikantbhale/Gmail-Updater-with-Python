#!/usr/bin/env python
# coding: utf-8

# In[4]:


def update_email(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index = email.index("@"+old_domain)
        new_mail=email[:index] + new_domain
        return new_mail
    else:
        return email
    
new_mail = update_email("laxmikantvbhale@gmail.com","gmail.com","@email.com")
print(new_mail)


# In[ ]:




