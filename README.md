# cyprus_medication

Project for preparing json database for the bot [FindPharmaCy_Bot](https://t.me/FindPharmaCy_Bot)

Link to [dataset](https://www.moh.gov.cy/moh/phs/phs.nsf/All/D715A6B6FC124276C2258AFB002C9B73?OpenDocument)


# Pipeline
1. Upload dataset
2. Convert to json.
3. Add to `drugs.json` using key `pricing_code`
4. Update `active.json` using Prepare active chapter
5. Combine `drugs_light.json` using script `make_drugs_light.py`


## ToDo
- [ ] Check package of eye drops and others
- [ ] Check how handle package emoji
- [ ] Pharmacist must check new medication in csv file
- [ ] Find key words using lemmatizaion and llm