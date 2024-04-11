SELECT_ALL = 'SELECT character_id, name FROM charactercreator_character;'


AVG_ITEM_WEIGHT_PER_CHARACTER = '''
    SELECT cc_char.name, SUM(ai.weight)
    FROM charactercreator_character as cc_char
    JOIN charactercreator_character_inventory as CC_inv
    ON cc_char.character_id = cc_inv.character_id
    JOIN armory_item as ai
    ON ai.item_id = cc_inv.item_id
    GROUP BY cc_char.character_id'''

# other sql queries, don't forget to assign them to varaiables

# # select from all from the table
# SELECT * 
# FROM charactercreator_character

# # select char_id and name fro table charactercreator_character
# SELECT character_id, name 
# FROM charactercreator_character

# SELECT *
# FROM charactercreator_character
# WHERE character_id > 80;


# SELECT character_id, name
# FROM charactercreator_character
# WHERE character_id = 80;

# SELECT character_id, name
# FROM charactercreator_character
# WHERE character_id >= 80 AND character_id <= 100;

# SELECT character_id, name
# FROM charactercreator_character
# WHERE character_id
# BETWEEN 5 AND 12;

# # Number of unqiue words in the databse # in column name
# SELECT 
# DISTINCT name
# FROM charactercreator_character

# # Group By
# # This groups up names which are the same with count
# SELECT name,
# COUNT(*)
# FROM charactercreator_character
# GROUP BY name

# SELECT name,
# COUNT(*)
# FROM charactercreator_character
# ORDER BY name

# # Grpuping by name and stating the count
# SELECT name,
# COUNT(*)
# FROM charactercreator_character
# GROUP BY name
# HAVING COUNT(*) =2

# #Ordering in desceding order
# SELECT name,
# COUNT(*)
# FROM charactercreator_character
# GROUP BY name
# HAVING COUNT(*) =2
# ORDER BY name 
# DESC

# # Joining tables
# SELECT * 
# FROM charactercreator_character
# JOIN charactercreator_mage

# # Join on ids
# SELECT * 
# FROM charactercreator_character
# JOIN charactercreator_mage
# ON charactercreator_character.character_id = charactercreator_mage.character_ptr_id


# # join on ids but from specific columns
# SELECT strength, has_pet
# FROM charactercreator_character
# JOIN charactercreator_mage
# ON charactercreator_character.character_id = charactercreator_mage.character_ptr_id

# # Rname columns 
# SELECT *
# FROM charactercreator_mage AS ccm
# LEFT JOIN charactercreator_character AS cc_char
# ON cc_char.character_id = ccm.character_ptr_id



# # Rename a column
# SELECT name,
# COUNT(*) AS num_characters
# FROM charactercreator_character AS ccm
# GROUP BY name
# HAVING num_characters=2


# # More joins
# SELECT *
# FROM charactercreator_character as cc_char
# JOIN charactercreator_character_inventory as CC_inv
# ON cc_char.character_id = cc_inv.character_id

# # MOre
# SELECT *
# FROM charactercreator_character as cc_char
# JOIN charactercreator_character_inventory as CC_inv
# ON cc_char.character_id = cc_inv.character_id
# JOIN armory_item as ai
# ON ai.item_id = cc_inv.item_id

# SELECT cc_char.name, ai.weight
# FROM charactercreator_character as cc_char
# JOIN charactercreator_character_inventory as CC_inv
# ON cc_char.character_id = cc_inv.character_id
# JOIN armory_item as ai
# ON ai.item_id = cc_inv.item_id

# # sum
# SELECT cc_char.name, SUM(ai.weight)
# FROM charactercreator_character as cc_char
# JOIN charactercreator_character_inventory as CC_inv
# ON cc_char.character_id = cc_inv.character_id
# JOIN armory_item as ai
# ON ai.item_id = cc_inv.item_id
# GROUP BY cc_char.character_id

# # average
# SELECT cc_char.name, AVERAGE(ai.weight)
# FROM charactercreator_character as cc_char
# JOIN charactercreator_character_inventory as CC_inv
# ON cc_char.character_id = cc_inv.character_id
# JOIN armory_item as ai
# ON ai.item_id = cc_inv.item_id
# GROUP BY cc_char.character_id

