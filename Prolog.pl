% Define possible values for each attribute
names([joshua, daniel, nicholas, ryan]).
ages([11, 12, 13, 14]).
shirts([black, red, green, blue]).
movies([horror, thriller, action, comedy]).
snacks([cookies, crackers, popcorn, chips]).

% Main predicate to solve the puzzle
solve(Solution) :-
    % Each attribute is represented by a list of length 4 (one value per person)
    names(Names),
    permutation(Names, [N1, N2, N3, N4]),
    
    ages(Ages),
    permutation(Ages, [A1, A2, A3, A4]),

    shirts(Shirts),
    permutation(Shirts, [S1, S2, S3, S4]),

    movies(Movies),
    permutation(Movies, [M1, M2, M3, M4]),

    snacks(Snacks),
    permutation(Snacks, [Sn1, Sn2, Sn3, Sn4]),

    % Clues
    (N1 = joshua; N4 = joshua),
    S1 = green,
    nth1(JoshuaPos, [N1, N2, N3, N4], joshua),
    nth1(JoshuaPos, [M1, M2, M3, M4], horror),
    A3 = 14,
    (Sn1 = cookies; Sn4 = cookies),
    (M1 = thriller; M4 = thriller),
    nth1(BlackPos, [S1, S2, S3, S4], black),
    nth1(YoungestPos, [A1, A2, A3, A4], 11),
    BlackPos < YoungestPos,
    nth1(ThrillerPos, [M1, M2, M3, M4], thriller),
    BlackPos + 1 =:= ThrillerPos,
    nth1(ComedyPos, [M1, M2, M3, M4], comedy),
    nth1(CrackersPos, [Sn1, Sn2, Sn3, Sn4], crackers),
    ComedyPos + 1 =:= CrackersPos,
    nth1(RedPos, [S1, S2, S3, S4], red),
    nth1(PopcornPos, [Sn1, Sn2, Sn3, Sn4], popcorn),
    nth1(NicholasPos, [N1, N2, N3, N4], nicholas),
    PopcornPos < RedPos, RedPos < NicholasPos,
    nth1(DanielPos, [N1, N2, N3, N4], daniel),
    JoshuaPos < NicholasPos, NicholasPos < DanielPos,

    % Solution format
    Solution = [
        [name: N1, age: A1, shirt: S1, movie: M1, snack: Sn1],
        [name: N2, age: A2, shirt: S2, movie: M2, snack: Sn2],
        [name: N3, age: A3, shirt: S3, movie: M3, snack: Sn3],
        [name: N4, age: A4, shirt: S4, movie: M4, snack: Sn4]
    ].

% Run the solution and print it
print_solution :-
    solve(Solution),
    write("Solution:"), nl,
    forall(member(Person, Solution), (
        write(Person), nl
    )).

% Initialization directive to execute print_solution at the start
:- initialization(print_solution).

