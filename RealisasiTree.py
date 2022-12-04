class PohonBiner:
    def __init__(self,A,L,R):
        self.A = A
        self.L = L
        self.R = R

    def __repr__(self):
        return "((%s,%s,%s))" % (repr(self.A), repr(self.L), repr(self.R))

def akar(P):
    return P.A

def left(P):
    return P.L

def right(P):
    return P.R

def make_pb(A,L,R):
    return PohonBiner(A,L,R)

def is_empty_tree(P):
    return P == None

def is_one_elmt(P):
    return not is_empty_tree(P) and is_empty_tree(right(P)) and is_empty_tree(left(P))

def is_uner_left(P):
    return not is_empty_tree(P) and not is_empty_tree(left(P)) and is_empty_tree(right(P))

def is_uner_right(P):
    return not is_empty_tree(P) and not is_empty_tree(right(P)) and is_empty_tree(left(P))

def is_biner(P):
    return not is_empty_tree(P) and not is_empty_tree(right(P)) and not is_empty_tree(left(P))

def is_exist_left(P):
    return not is_empty_tree(P) and not is_empty_tree(left(P))

def is_exist_right(P):
    return not is_empty_tree(P) and not is_empty_tree(right(P))

def nb_elmt(P):
    if is_empty_tree(P):
        return 0
    else :
        return nb_elmt(right(P)) + nb_elmt(left(P))

def nb_daun(P):
    if is_one_elmt(P):
        return 1
    else :
        if is_biner(P):
            return nb_daun(left(P)) + nb_daun(right(P))
        elif is_uner_right(P):
            return nb_daun(right(P))
        elif is_uner_left(P):
            return nb_daun(right(P))

def rep_prefix(P):
    if is_one_elmt(P):
        return [akar(P)]
    else :
        if is_biner(P):
            return [akar(P)] + rep_prefix(right(P)) + rep_prefix(left(P))
        elif is_uner_left(P):
            return [akar(P)] + rep_prefix(left(P))
        elif is_uner_right(P):
            return [akar(P)] + rep_prefix(right(P))

def is_member(P,X):
    if is_empty_tree(P):
        return False
    else :
        if akar(P) == X:
            return True
        else :
            if is_biner(P):
                return is_member(left(P),X) or is_member(right(P),X)
            elif is_uner_right(P):
                return is_member(right(P),X)
            elif is_uner_left(P):
                return is_member(left(P),X)
            else :
                return False

def is_skew_left(P:PohonBiner):
    if is_one_elmt(P) or is_empty_tree(P):
        return False
    else :
        if is_uner_left(P):
            if is_one_elmt(left(P)):
                return True
            else :
                if is_uner_left(left(P)):
                    return is_skew_left(left(P))
                else :
                    return False
        else :
            return False

def is_skew_right(P:PohonBiner):
    if is_one_elmt(P) or is_empty_tree(P):
        return False
    else :
        if is_uner_right(P):
            if is_one_elmt(right(P)):
                return True
            else :
                if is_uner_right(right(P)):
                    return is_skew_right(right(P))
                else :
                    return False
        else :
            return False
            
            
print(P)
print(rep_prefix(P))
print(nb_daun(P))
print(nb_elmt(P))
print(is_uner_left(P))
print(is_exist_right(P))
print(is_member(P,4))
print(is_skew_left(P))
print(is_skew_right(P))
