(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (ordered? s)
  (cond ((null? s) True)
       ((null? (cdr s)) True)
       ((<= (car s) (cadr s)) (ordered? (cdr s)))
       (else False)
  )
)

(define (nodots s)
  (if (null? s)
      nil
      (cond  (  (integer? s) (list s)  )
             (  (pair? (car s))  (cons (nodots (car s)) (nodots (cdr s)))  )
             (  (null? (cdr s)) s  )
             (  else (cons (car s) (nodots (cdr s)))  )
      )
  )
)

; Sets as sorted lists

(define (empty? s) (null? s))

(define (contains? s v)
    (cond (  (empty? s) False  )
          (  (> (car s) v) False  )
          (  (= (car s) v) True  )
          (  else (contains? (cdr s) v))
    )
)

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (add s v)
    (cond (  (empty? s) (list v)  )
          (  (> (car s) v) (cons v s)  )
          (  (= (car s) v) s  )
          (  (<(car s) v) (cons (car s) (add (cdr s) v))  )
          ))

(define (intersect s t)
    (cond (  (or (empty? s) (empty? t)) nil  )
          (  (= (car s) (car t)) (cons (car s) (intersect (cdr s) (cdr t)))  )
          (  (< (car s) (car t)) (intersect (cdr s) t)  )
          (  (> (car s) (car t)) (intersect (cdr t) s)  )
          ))

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
    (cond ((empty? s) t)
          ((empty? t) s)
          (  (= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t)))  )
          (  (< (car s) (car t)) (cons (car s) (union (cdr s) t))  )
          (  (> (car s) (car t)) (cons (car t) (union s (cdr t)))  )          
          ))

; A data abstraction for binary trees where nil represents the empty tree
(define (tree label left right) (list label left right))
(define (label t) (car t))
(define (left t) (cadr t))
(define (right t) (caddr t))
(define (empty? s) (null? s))
(define (leaf label) (tree label nil nil))

(define (in? t v)
    (cond ((empty? t) False)
          (  (= (label t) v) True  )
          (  (> (label t) v) (in? (left t) v)  )
          (  (< (label t) v) (in? (right t) v)  )
          ))

; Equivalent Python code, for your reference:
;
; def contains(t, v):
;     if t is BST.empty:
;         return False
;     elif t.entry == v:
;         return True
;     elif v < t.entry:
;         return contains(t.left, v)
;     elif v > t.entry:
;         return contains(t.right, v)

(define (as-list t)
    (cond ((empty? t) nil)
          (  else (union (add (as-list (left t)) (label t)) (as-list (right t)))  )
          ))
;; Extra Questions

(define (cadr s) (car (cdr s)))
(define (caddr s) (car (cdr (cdr s))))

; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (addend s) (cadr s))
(define (augend s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
(cond ((or (=number? m1 0) (=number? m2 0)) 0)
      ((=number? m1 1) m2)
      ((=number? m2 1) m1)
      ((and (number? m1) (number? m2)) (* m1 m2))
      (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
(define (multiplier p) (cadr p))
(define (multiplicand p) (caddr p))

(define (derive-sum expr var)
  (  make-sum (derive (addend expr) var) (derive (augend expr) var)  )
  )

(define (derive-product expr var)
  (  make-sum ( make-product (derive (multiplier expr) var) (multiplicand expr) ) ( make-product (derive (multiplicand expr) var) (multiplier expr) )  )
  )

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
(cond (  (number? base) (expt base exponent)  )
      (  (=number? exponent 0) 1  )
      (  (=number? exponent 1) base  )      
      (else (list '^ base exponent))))

(define (base exp)
  (cadr exp)
  )

(define (exponent exp)
  (caddr exp)
  )

(define (exp? exp)
  (and (list? exp) (eq? (car exp) '^))
  )

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

(define (derive-exp exp var)
  ( make-product (exponent exp) (make-exp (base exp) (- (exponent exp) 1)) )
  )
