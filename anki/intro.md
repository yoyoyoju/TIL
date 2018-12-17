# ANKI

### Decks
* create decks
* `Deck::Subdeck`
* `German::Words`

### Fields
* add field (can have  more than two fields)
* for exampe `word` and `meaning` `example`


### Card types
* blueprint of card
* two templets: question and answer
```
{{word}}
{{meaning}}<br>
exampe: {{example}}
```

### Note types
* basic: has front and back fields (one card)
* basic and reversed: two cards 
* basic optional reversed: may have reverse card
* Cloze: has cloze deletion
* can be added in `Tools` -> `Manage Note Types`

### Cloze Deletion
* hide some words in a sentence
* select Cloze note type
```
{{c2::Canberra}} was founded in {{c1::1913}}.
```
* one can give a hint
```
{{c1::Canberra::city}} was founded in 1913.
```

### check your answer
* the front template:
```
{{German word}}
{{type:article}}
```

