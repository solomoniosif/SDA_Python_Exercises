
prod1 = "Lenovo Ideapad Slim 7"
prod2 = "ASUS TUF A15 FA506IU"


def name_to_url(name):
  lower_name = ''.join([ch.lower() for ch in name])
  diacritics_removed = ""
  for ch in lower_name:
    if ch in ['ă', 'â']:
      diacritics_removed += 'a'
    elif ch == 'î':
      diacritics_removed += 'i'
    elif ch == 'ț':
      diacritics_removed += 't'
    elif ch == 'ș':
      diacritics_removed += 's'
    else:
      diacritics_removed += ch
  spaces_removed = '-'.join(diacritics_removed.split())
  unallowed_charachters = ['„', '<', '>', '#', '%', '{', '}', '\\', '|', '^', '[', ']', '`', '!', '$', '%', '\'', '(', ')', '*', '+', ',', '/', ':', ';', '=', '?', '@']
  for ch in spaces_removed:
    if ch in unallowed_charachters:
      spaces_removed.replace(ch, "")
  return spaces_removed


print(name_to_url(prod2))

