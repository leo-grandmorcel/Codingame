nb_associations = int(input())
nb_filenames = int(input())
mime_types = {}
for _ in range(nb_associations):
    extension, mime_type = input().split()
    mime_types[extension.upper()] = mime_type

for _ in range(nb_filenames):
    filename = input()
    if "." in filename:
        print(mime_types.get(filename.split(".")[-1].upper(), "UNKNOWN"))
    else:
        print("UNKNOWN")
