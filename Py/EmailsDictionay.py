def email_list(domains):
        emails = []
        for dom,users in domains.items():
            for user in users:
                emails.append(user+"@"+dom)
        return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))