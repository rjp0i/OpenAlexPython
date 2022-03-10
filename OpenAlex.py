

# UVA institutional ID:  I51556381
    
#info about institution
#https://api.openalex.org/institutions?filter=display_name.search:University%20of%20Virginia

#works by institution
#https://api.openalex.org/works?filter=institutions.id:I51556381


import requests
import json




"""
Section 1: Data for UVA as an institution
"""

# request = requests.get(f'https://api.openalex.org/institutions?filter=display_name.search:University%20of%20Virginia')

# json_data = json.loads(request.text)
# #print(json_data)

# for keys, values in json_data.items():
#     print(keys)
    
# results = json_data['results']


# # there are a bunch of results for institutions with a name similar to "university of virginia". Filtering out just the right ones
# uva_data = results[0]
# uva_health_data = results[1] 
# uva_dept_of_urology = results[2]   # why is the separate?  I don't know why

# # potentially intersting UVA data?
# print(f"Total number of UVA publications (in OpenAlex): {uva_data['works_count']}")
# print(f"Total number of citations of UVA publications (in OpenAlex): {uva_data['cited_by_count']}")

# print("Publication counts and citations per year")

# counts_by_year = uva_data['counts_by_year']
# for year in counts_by_year:
#     print(f"Year: {year['year']}, Publications: {year['works_count']}, Citations: {year['cited_by_count']}")
    
    
    
"""
Section 2: Works

There are 39790 affiliated authors at UVA in the dataset. I can only include 10,000 in the results.
The ability to include all is not currently available in the API (but is in the works)

"""
# request = requests.get('https://api.openalex.org/authors?filter=last_known_institution.id:I51556381,cited_by_count:>0&page=3&per-page=200')
# json_data = json.loads(request.text)
# # does this seem like too many?
# print(f"# authors with last known affiliation of UVA: {json_data['meta']['count']}")

# authors = json_data['results']
# print(f"Authors on current page:")
# for author in authors:
#     print(author['display_name'])



"""
Section 3: Author
"""
# author ID of Brad Cox = A3037630497
request = requests.get(f'https://api.openalex.org/authors/A3037630497')
json_data = json.loads(request.text)

print(f"Numbers for {json_data['display_name']}: ")
print(f"Publications: {json_data['works_count']}")
print(f"Citations: {json_data['cited_by_count']}")


###START HERE WITH /works
## figure out how to request works by author



