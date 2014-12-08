#! /usr/bin/env python2.7
# -*- coding: utf-8 -*-

import portfolio

"""
Uniform portfolio

Jendrik Seipp, Manuel Braun, Johannes Garimort and Malte Helmert
"Learning Portfolios of Automatically Tuned Planners" in ICAPS 2012.
"""

CONFIGS = [
    # airport
    (85, [u'--landmarks', u'lmg=lm_rhw(only_causal_landmarks=false,disjunctive_landmarks=true,conjunctive_landmarks=true,no_orders=false,lm_cost_type=2,cost_type=2)', u'--heuristic', u'hCea=cea(cost_type=2)', u'--heuristic', u'hLM,hFF=lm_ff_syn(lmg,admissible=true)', u'--search', u'lazy(alt([single(hLM),single(hLM,pref_only=true),single(hFF),single(hFF,pref_only=true),single(hCea),single(hCea,pref_only=true)], boost=0),preferred=[hLM,hCea],reopen_closed=false,cost_type=2,bound=BOUND)']),
    # depot
    (85, [u'--landmarks', u'lmg=lm_hm(only_causal_landmarks=false,disjunctive_landmarks=true,conjunctive_landmarks=true,no_orders=false,m=1)', u'--heuristic', u'hCea=cea(cost_type=2)', u'--heuristic', u'hLM=lmcount(lmg,admissible=true)', u'--search', u'lazy(alt([single(hLM),single(hLM,pref_only=true),single(hCea),single(hCea,pref_only=true)], boost=100),preferred=[hCea],reopen_closed=false,cost_type=2,bound=BOUND)']),
    # driverlog
    (85, [u'--landmarks', u'lmg=lm_rhw(only_causal_landmarks=false,disjunctive_landmarks=true,conjunctive_landmarks=true,no_orders=true,lm_cost_type=2,cost_type=1)', u'--heuristic', u'hLM,hFF=lm_ff_syn(lmg,admissible=true)', u'--search', u'lazy(alt([single(hLM),single(hLM,pref_only=true),single(hFF),single(hFF,pref_only=true)], boost=0),preferred=[hLM],reopen_closed=false,cost_type=2,bound=BOUND)']),
    # freecell
    (85, [u'--landmarks', u'lmg=lm_hm(only_causal_landmarks=false,disjunctive_landmarks=true,conjunctive_landmarks=true,no_orders=true,m=1)', u'--heuristic', u'hLM=lmcount(lmg,admissible=true)', u'--search', u'eager(single(sum([g(),weight(hLM, 5)])),preferred=[],reopen_closed=true,pathmax=false,cost_type=1,bound=BOUND)']),
    # grid
    (85, [u'--landmarks', u'lmg=lm_rhw(only_causal_landmarks=false,disjunctive_landmarks=true,conjunctive_landmarks=true,no_orders=true,lm_cost_type=1,cost_type=2)', u'--heuristic', u'hCg=cg(cost_type=2)', u'--heuristic', u'hLM,hFF=lm_ff_syn(lmg,admissible=true)', u'--search', u'lazy(alt([single(sum([g(),weight(hLM, 10)])),single(sum([g(),weight(hLM, 10)]),pref_only=true),single(sum([g(),weight(hFF, 10)])),single(sum([g(),weight(hFF, 10)]),pref_only=true),single(sum([g(),weight(hCg, 10)])),single(sum([g(),weight(hCg, 10)]),pref_only=true)], boost=1000),preferred=[hLM,hCg],reopen_closed=false,cost_type=2,bound=BOUND)']),
    # logistics00
    (85, [u'--heuristic', u'hCea=cea(cost_type=1)', u'--search', u'lazy(alt([single(sum([g(),weight(hCea, 10)])),single(sum([g(),weight(hCea, 10)]),pref_only=true)], boost=2000),preferred=[hCea],reopen_closed=false,cost_type=1,bound=BOUND)']),
    # miconic-fulladl
    (85, [u'--heuristic', u'hFF=ff(cost_type=1)', u'--search', u'lazy(alt([single(hFF),single(hFF,pref_only=true)], boost=5000),preferred=[hFF],reopen_closed=false,cost_type=1,bound=BOUND)']),
    # mprime
    (85, [u'--heuristic', u'hCea=cea(cost_type=2)', u'--search', u'lazy(alt([single(sum([g(),weight(hCea, 5)])),single(sum([g(),weight(hCea, 5)]),pref_only=true)], boost=1000),preferred=[hCea],reopen_closed=false,cost_type=2,bound=BOUND)']),
    # optical-telegraphs
    (85, [u'--heuristic', u'hCg=cg(cost_type=1)', u'--heuristic', u'hFF=ff(cost_type=1)', u'--search', u'lazy(alt([single(sum([g(),weight(hFF,10)])),single(sum([g(),weight(hFF,10)]),pref_only=true),single(sum([g(),weight(hCg, 10)])),single(sum([g(),weight(hCg,10)]),pref_only=true)],boost=100),preferred=[hCg],reopen_closed=false,cost_type=1,bound=BOUND)']),
    # pathways
    (85, [u'--landmarks', u'lmg=lm_hm(only_causal_landmarks=false,disjunctive_landmarks=true,conjunctive_landmarks=false,no_orders=true,m=1,lm_cost_type=0,cost_type=2)', u'--heuristic', u'hLM,hFF=lm_ff_syn(lmg,admissible=true)', u'--search', u'lazy(alt([single(hLM),single(hLM,pref_only=true),single(hFF),single(hFF,pref_only=true)], boost=5000),preferred=[hLM],reopen_closed=false,cost_type=0,bound=BOUND)']),
    # philosophers
    (85, [u'--heuristic', u'hCg=cg(cost_type=2)', u'--search', u'lazy(alt([single(sum([g(),weight(hCg, 10)])),single(sum([g(),weight(hCg, 10)]),pref_only=true)], boost=0),preferred=[hCg],reopen_closed=false,cost_type=2,bound=BOUND)']),
    # pipesworld-notankage
    (85, [u'--landmarks', u'lmg=lm_merged([lm_rhw(),lm_hm(m=1)],only_causal_landmarks=false,disjunctive_landmarks=false,conjunctive_landmarks=true,no_orders=false)', u'--heuristic', u'hFF=ff(cost_type=0)', u'--heuristic', u'hLM=lmcount(lmg,admissible=true)', u'--search', u'lazy(alt([single(sum([g(),weight(hFF, 10)])),single(sum([g(),weight(hFF, 10)]),pref_only=true),single(sum([g(),weight(hLM, 10)])),single(sum([g(),weight(hLM, 10)]),pref_only=true)], boost=500),preferred=[hFF],reopen_closed=false,cost_type=2,bound=BOUND)']),
    # pipesworld-tankage
    (85, [u'--heuristic', u'hFF=ff(cost_type=1)', u'--search', u'lazy(alt([single(sum([g(),weight(hFF, 7)])),single(sum([g(),weight(hFF, 7)]),pref_only=true)], boost=5000),preferred=[hFF],reopen_closed=false,cost_type=1,bound=BOUND)']),
    # psr-large
    (85, [u'--heuristic', u'hAdd=add(cost_type=0)', u'--search', u'lazy(alt([single(hAdd),single(hAdd,pref_only=true)], boost=0),preferred=[hAdd],reopen_closed=true,cost_type=0,bound=BOUND)']),
    # rovers
    (85, [u'--landmarks', u'lmg=lm_hm(only_causal_landmarks=false,disjunctive_landmarks=true,conjunctive_landmarks=true,no_orders=false,m=1,lm_cost_type=2,cost_type=0)', u'--heuristic', u'hLM,hFF=lm_ff_syn(lmg,admissible=true)', u'--search', u'lazy(alt([tiebreaking([sum([g(),weight(hLM, 10)]),hLM]),tiebreaking([sum([g(),weight(hLM, 10)]),hLM],pref_only=true),tiebreaking([sum([g(),weight(hFF, 10)]),hFF]),tiebreaking([sum([g(),weight(hFF, 10)]),hFF],pref_only=true)], boost=200),preferred=[hLM],reopen_closed=true,cost_type=2,bound=BOUND)']),
    # satellite
    (85, [u'--heuristic', u'hCg=cg(cost_type=2)', u'--search', u'lazy(alt([single(hCg),single(hCg,pref_only=true)], boost=0),preferred=[hCg],reopen_closed=true,cost_type=2,bound=BOUND)']),
    # schedule
    (85, [u'--landmarks', u'lmg=lm_hm(only_causal_landmarks=false,disjunctive_landmarks=true,conjunctive_landmarks=false,no_orders=true,m=1,lm_cost_type=1,cost_type=0)', u'--heuristic', u'hLM,hFF=lm_ff_syn(lmg,admissible=true)', u'--search', u'lazy(alt([single(hLM),single(hLM,pref_only=true),single(hFF),single(hFF,pref_only=true)], boost=1000),preferred=[hLM,hFF],reopen_closed=false,cost_type=1,bound=BOUND)']),
    # storage
    (85, [u'--landmarks', u'lmg=lm_hm(only_causal_landmarks=false,disjunctive_landmarks=true,conjunctive_landmarks=false,no_orders=true,m=1)', u'--heuristic', u'hCg=cg(cost_type=1)', u'--heuristic', u'hLM=lmcount(lmg,admissible=true)', u'--search', u'lazy(alt([single(hLM),single(hLM,pref_only=true),single(hCg),single(hCg,pref_only=true)], boost=0),preferred=[hCg],reopen_closed=false,cost_type=1,bound=BOUND)']),
    # tpp
    (85, [u'--landmarks', u'lmg=lm_hm(only_causal_landmarks=false,disjunctive_landmarks=true,conjunctive_landmarks=false,no_orders=true,m=1,lm_cost_type=0,cost_type=2)', u'--heuristic', u'hLM,hFF=lm_ff_syn(lmg,admissible=true)', u'--search', u'lazy(alt([single(sum([g(),weight(hLM, 10)])),single(sum([g(),weight(hLM, 10)]),pref_only=true),single(sum([g(),weight(hFF, 10)])),single(sum([g(),weight(hFF, 10)]),pref_only=true)], boost=500),preferred=[hLM],reopen_closed=false,cost_type=0,bound=BOUND)']),
    # trucks-strips
    (85, [u'--heuristic', u'hFF=ff(cost_type=1)', u'--search', u'lazy(alt([single(sum([weight(g(), 2),weight(hFF, 3)])),single(sum([weight(g(), 2),weight(hFF, 3)]),pref_only=true)], boost=5000),preferred=[hFF],reopen_closed=true,cost_type=1,bound=BOUND)']),
    # zenotravel
    (85, [u'--heuristic', u'hCg=cg(cost_type=1)', u'--search', u'lazy(tiebreaking([sum([g(),weight(hCg, 2)]),hCg]),preferred=[],reopen_closed=true,cost_type=1,bound=BOUND)'])
]

portfolio.run(configs=CONFIGS, optimal=False, timeout=1800)
