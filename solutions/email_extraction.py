def email(str):
    '''To extract emails'''
    import re
    emailRegex = re.compile(r'''
    # some.+_thing@(\d{2,5})?.com
    # General Email Regex (RFC 5322 Official Standard)
    (?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*
    |"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|
    \\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+
    [a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|
    [01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|
    [a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|
    \\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])
    ''', re.VERBOSE)
    emails = emailRegex.findall(str)
    return [email for email in emails]

print(email('E-mail: madamson@sncn.netAll Track Int'))