(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

(define (enumerate s)
  (define (helper s i) 
    (if (eq? s nil) nil
      (cons (list i (car s)) (helper (cdr s) (+ i 1)))
  ))
  (helper s 0)
  )

(define (cons-all first rests)
  (if (eq? rests nil) nil
    (
     cons (cons first (car rests)) (cons-all first (cdr rests))
    )
  )
)

(define (list-change total denoms)
  (cond (  (< total 0) nil  )
        (  (= total 0) '(())  )
        (  (eq? denoms nil) nil  )
        (  else
          (if (not (eq? nil (list-change (- total (car denoms)) denoms)))
              (append 
                (cons-all (car denoms) (list-change (- total (car denoms)) denoms)) 
                (list-change total (cdr denoms)) )
              ( list-change total (cdr denoms)  )  
          )            
       )
   )
)


(define (zip pairs)
  (if (eq? pairs nil) '(()())
    (list (cons (caar pairs) (car (zip (cdr pairs))) )
          (cons (car (cdar pairs)) (car (cdr (zip (cdr pairs)))) )
    )
  )  
)


(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((quoted? expr)
         ; BEGIN PROBLEM 19
         expr
         ; END PROBLEM 19
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (append (list form params) (map let-to-lambda body))
           ; END PROBLEM 19
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 19
           (append  (list ( append (list 'lambda (car (zip values))) (map let-to-lambda body)) )   (map let-to-lambda (cadr (zip values)))  )
           ; END PROBLEM 19
           ))
        (else
         ; BEGIN PROBLEM 19
         (map let-to-lambda expr)
         ; END PROBLEM 19
         )))

(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))


(define (map proc items)
  (if (eq? items nil) nil
     (cons (proc (car items)) (map proc (cdr items)))
  )
)