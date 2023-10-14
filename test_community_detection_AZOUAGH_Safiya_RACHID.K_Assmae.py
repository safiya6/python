###AZOUAGH Safiya RACHID.K Assmâe

##################################
# tableau pour tester les assert #
##################################
list_friends= ["Alice", "Bob", "Charlie", "Bob","Dominique", "Alice","Dominique","Bob"]

##########################
#test fonction liste_amis#
##########################

def test_create_network():
    def test_create_network():
    assert not create_network(list_friends)=={"Julie":["Ahmed","Wassima","Rizlaine","Salma"]}
    assert not create_network(list_friends)=={'Alice': ['Bob', 'Dominique'],'Jean': ['Alice', 'Charlie', 'Dominique'],'Charlie': ['Bob'],'Dominique': ['Alice', 'Bob']}
    assert create_network(list_friends)=={'Alice': ['Bob', 'Dominique'],'Bob': ['Alice', 'Charlie', 'Dominique'],'Charlie': ['Bob'],'Dominique': ['Alice', 'Bob']}
    print("test OK ")
    
###############################   
#test de la fontion get_people#
###############################


def test_get_people(network):
    assert not get_people(list_friends)==['Safiya','Assmae']
    assert get_people(list_friends)==['Alice', 'Bob', 'Charlie', 'Dominique']
    print("test OK")
    
#################################
#test de la fonction are_friend #
#################################
def test_are_friends():
    assert are_friends((create_network(list_friends)),'Alice','Charlie')==False
    assert are_friends((create_network(list_friends)),'Alice','Bob')==True
    assert not are_friends((create_network(list_friends)),'Alice','Dominique')==False 
    print("test Ok")
    
######################################    
#test de la fonction all_his_friends #
######################################


def test_all_his_friends():
    assert all_his_friends((create_network(list_friends)),'Alice',['Dominique','Bob'])==True 
    assert all_his_friends((create_network(list_friends)),'Alice',['Mohammed','Alya'])==False  
    print ("test Ok")

####################################    
#test de la fonction is_a_community#   
####################################


def test_is_a_community():
    assert is_a_community((create_network(list_friends)),["Alice","Bob","Charlie"])==False
    assert is_a_community((create_network(list_friends)),["Alice","Bob","Dominique"])== True 
    print("test OK")

####################################
#test de la fonction find_community#
####################################


def test_find_community():
    assert find_community((create_network(list_friends)),["Alice", "Bob", "Charlie", "Dominique"])==["Alice", "Bob", "Dominique"]
    assert find_community((create_network(list_friends)),["Charlie", "Alice", "Bob", "Dominique"])==['Charlie','Bob']
    assert not find_community((create_network(list_friends)),["Charlie","Alice", "Dominique"])==["Bob","Charlie"]
    print ("test OK")
    
    
#####################################################
#test de la fonction order_by_decreasing_popularity # 
#####################################################

def test_order_by_decreasing_popularity():
    assert order_by_decreasing_popularity((create_network(list_friends)),['Bob','Alice','Dominique'])==["Bob","Dominique","Alice"] 
    assert order_by_decreasing_popularity((create_network(list_friends)),["Bob",'Alice'])==["Bob","Alice"]
    assert not order_by_decreasing_popularity((create_network(list_friends)),["Bob","Alice","Charlie"])==["Charlie","Bob","Alice"]
    print ("le test est OK")
        
####################################################
# test de la fonction find_by_decreasing_popularity#
####################################################


def test_find_community_by_decreasing_popularity():
    assert find_community_by_decreasing_popularity((create_network(list_friends))) ==['Bob','Dominique','Alice']
    assert not find_community_by_decreasing_popularity((create_network(list_friends)))==['Bob','Dominique','Alice','Charlie']
    print ("test Ok")
    

    
######################################################    
#test de la fonction test_find_community_from_person #
######################################################

def test_find_community_from_person():
    assert find_community_from_person((create_network(list_friends)),'Alice')== ['Alice', 'Bob', 'Dominique']
    assert find_community_from_person((create_network(list_friends)),'Bob')== ['Bob','Dominique','Alice']
    assert not fin_community_from_person((create_network(list_friends)),'Bob')==['Bob']
    print ('le test est OK')
 
 ##################################################
 #   test de la fonction test_max_community       #
 ##################################################

    
def test_find_max_community():
    assert find_max_community((create_network(list_friends)))==['Alice','Bob','Dominique']
    assert not find_max_community((create_network(list_friends)))==['Alice','Bob','Charlie']
    assert not find_max_community((create_network(list_friends)))==['Alice']
    print('test OK')
    
##AZOUAGH Safiya RACHID.K Assmâe