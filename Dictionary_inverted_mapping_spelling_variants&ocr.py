#!/usr/bin/env python
# coding: utf-8


inverted_mapping_universities_spelling ={
   
    #  New York
    
    "New School": ["New School for Social Research", 
                   "New School For Social Research", 
                   "New School University"
                  ],
    "New York University": ["New York University"],

    "New York University - Dep. Philosophy": ["New York University Department Philosophy"],

    "New York University - School Ed. div.": ["New York University School Education Division Historical and Philosophic Foundations"],

    "New York University - Dep. Hist-Phil. Ed.": ["New York University Department History and Philosophy Education"],


    "CUNY": ["City University New York"],

    "CUNY - Graduate Center": ["City University New York Graduate School and University Center"],


    "SUNY - Albany": ["State University New YorkAlb", "State University New York Albany", 
                      "State University New YorkAlbany", "UniversityAlbany", "University Albany", 
                      "State University New York Alb"
                     ],


    "SUNY - Buffalo": ["State University New YorkBuffal", "State University New York Buffalo", 
                       "State UniversityNew YorkBuffalo", "State University New YorkB?falo",
                       "State University New YorkBuffalo","State UniversityBuffalo", "UniversityBuffalo", 
                       "University Buffalo", "State University New York B?falo", "State University Buffalo",
                       "State University New York Buffal"
                      ],

    "SUNY - Binghamton": ["State University New York Binghamton", 
                          "State University New YorkBinghamton", 
                          "Binghamton University"
                         ],

    "SUNY - Stony Brook": ["State University New York Stony Brook", 
                           "State University New YorkStony Brook", 
                           "Stony Brook University"
                          ],

    "Syracuse University": ["Syracuse University"],

    "Columbia University": ["Columbia University"],

    "Columbia University - TC": ["Columbia University Teachers College"],
    
    "Cornell University": ["Cornell University"],
    
    "Fordham University": ["Fordham University"],
    
    "University of Rochester": ["University Rochester"],
    
    "Rockefeller University": ["Rockefeller University"],
    
    "St. Bonaventure University": ["Franciscan Institute St. Bonaventure University"],
    
    "St. John-s University": ["St. Johns University"],
    
    
    
    
    
    # Pennsylvania
    
    "Bryn Mawr College": ["Bryn Mawr College"],
    
    "Duquesne University": ["Duquesne University"],
    
    "Lehigh University": ["Lehigh University"],
    
    "Pennsylvania State University":["Pennsylvania State University"],
    
    "Temple University":["Temple University"],
    
    "University of Pennsylvania": ["University Pennsylvania"],
    
    "University of Pittsburgh":["University Pittsburgh", "University Pittsburg"],
    
    
    
    
    
    # New Jersey
    
    "Princeton University": ["Princeton University"],
    
    "Rutgers University": ["Rutgers State University New J", 
                           "Rutgers State University New Jersey", 
                           "Rutgers University"
                          ],
    
    
    
    # California
    
    
    "UC - Berkeley": ["University CaliforniaBerkley", "University CaliforniaBerkeley", 
                      "University California Berkeley", "University Calif ornia Berkeley", 
                      "Group in Logic and Methodology Science University California Berkeley", 
                      "University California Berkley"
                     ],


    "University of California": ["University California"],

    "UC - Riverside": ["Univertsity California Riverside", "University Calif ornia Riverside", 
                       "University California Riverside", "University CaliforniaRiverside"],
    "UC - San Diego":["University California San Diego", "University CaliforniaSan Diego"],

    "UC - Santa Barbara": ["University CaliforniaSanta Bar", "University Calif ornia Santa Barbara", 
                          "University Calif onia Santa Barbara", "University California Santa Barbara", 
                          "University CaliforniaSanta Barbara", "University California Santa Bar"],

    "UC - La Jolla": ["University California La Jolla"],
    "UC - Davis":["University Calif ornia Davis", "University California Davis", 
                  "University CaliforniaDavis"],
    "UC - Irvine":["University Calif ornia Irvine", "University California Irvine", "University CaliforniaIrvine"],
    "UC - LA": ["University Calif ornia Los Angeles", "University California Los Angeles:>", 
                "University CaliforniaLos Angeles", "University California Los Angeles"
               ],


    "University of Southern California": ["University Southern California", "university Southern California"],
    
    
    "Claremont Graduate School": ["Claremont Graduate School", 
                                  "Claremont Graduate University", 
                                  "Claremont Graduate School and University Center"
                                 ],
    
    
    "Stanford University": ["Stanford University"],
    
    
    
    # Indiana
    
    
    "Purdue University":["Purdue University"],
    
    "University of Notre Dame":["University Notre Dame", "Notre Dame University"],
    
    "Indiana University - Bloomington": ["Indiana University","Indian? University", 
                                         "Indiana UniversityBloomington Department History and Philosophy Science", 
                                         "Indiana UniversityBloomington", 
                                         "Indiana University Bloomington Department History and Philosophy Science", 
                                         "Indiana University Bloomington"
                                        ],
    
    
    
    
    # Ohio
    
    
    "Bowling Green State University": ["Bowling Green State University"],
    
    "Case Western Reserve University": ["Case Western Reserve University"],
    
    "Ohio State University": ["Ohio State University"],
    
    "University of Cincinnati": ["University Cincinnati"],
    
    
    
    
    # Massachussett
    
    
    
    "University Massachusetts": ["University Massachusetts"],

    "University Massachusetts - Amherst": ["University Massachusetts Amherst", "University MassachusettsAmherst", 
                                           "University Massachusetts atAmherst", "University MassachusettsAmtierst", 
                                           "University Massachusetts Am", "University MassachusettsAmhe", 
                                           "University Massachusetts Amtierst", "University Massachusetts Amhe"
                                          ],


    "Boston University": ["Boston University"],

    "Boston College": ["Boston Coll?ge", "Boston College"],




    "MIT":["Massachusetts Institute Technology"],
    
    "Brandeis University": ["Brandeis University"],
    
    "Harvard University": ["Harvard University"],
    
    "Radcliffe College": ["Radcliffe College"],
    
    
    
    
    # Maryland
    
    
    "University of Maryland": ["University Maryland"],
    
    
    "University of Maryland - College Park": ["University Maryland College Park"],
    
    "Johns Hopkins University": ["Johns Hopkins University", "John Hopkins University"],
    
    
    
    # North Carolina
    
    
    
    "University of North Carolina": ["University North Carolina"],
                                    
    "University of North Carolina - Chapel Hill": ["University North CarolinaChapel Hill", 
                                  "University North Carolina Chapel Hill"
                                 ],
    
    "Duke University":["Duke University"],
    
    
    
    # South Carolina

    
    "University of South Carolina": ["University South Carolina"],
    
    
    
    # Georgia
    
    
    
    "Emory University": ["Emory University"],
    
    "University of Georgia": ["University Georgia"],
    
    "University of Georgia - Athens": ["University Georgia Athens"],
    
    
    
    
    
    # Colorado
    
    
    "University of Colorado": ["University Colorado"],
    "University of Colorado - Boulder": ["University Colorado Boulder", "University ColoradoBoulder", 
                                         "University ColoradoBoulde", "University Colorado Boulde"],
    
    
    # Texas
    
    
    "University of Texas": ["University Texas"],
    "University of Texas - Austin": ["University TexasAustin", "University Texas Austin"],
    
    "University of Dallas": ["University Dallas"],
    
    "Rice University": ["jRice University", "Rice University", "William Marsh Rice University"],
    
    
    
    
    # Missouri
    
    
    
    "Washington University (St. Louis)": [ "Washington University", 
                                          "Washington University St. Louis", 
                                          "Washington University in St. Louis"
                                         ],
    
    "St. Louis University": ["St. Louis University", "Saint Louis University"],
    
    "University Missouri - Columbia": ["University Missouri", 
                                       "University MissouriColumbia", 
                                       "university Missouri Columbia", 
                                       "University Missouri Columbia", 
                                       "University Missouri? Columbia", 
                                       "University Missouri?Columbia",
                                       "University Missouri  Columbia"
                                       
                           ],
    
    # Wisconsin
    
    
    "University of Wisconsin (Madison)": ["University Wisconsin", 
                                       "University Wisconsin Madison", 
                                       "University WisconsinMadison"
                                      ],
    
    "Marquette University": ["Marquette University"],
    
    
    
    
    # Connecticut
    
    "University of Connecticut": ["University Connecticu t", 
                               "University Connecticut"],
    
    "Yale University": ["Yale University"],
    
    
    
    # Washington D.C.
    
    
    "American University": ["Amercian University", "American University"],
    "Catholic University of America" : ["Catholic University America"],
    
    "Georgetown University": ["Georgetown University"],
    
    
    
    # Tennessee
    
    "Vanderbilt University": ["Vanderb?t University", "Vanderbilt University"],

    "University of Memphis": ["University Memphis"],


    "University of Tennessee": ["University Tennessee"],


    "University of Tennessee - Knoxville": ["University TennesseeKnoxviUe", "University TennesseeKnoocville",
                                            "University TennesseeKnoxville", "University Tennessee Knoxville",
                                            "University Tennessee Knoocville", "University Tennessee KnoxviUe"
                                        ],
    
    
    
    # Michigan
    
    
    
    "Wayne State University": ["Wayne State University"],


    "University of Michigan":["University Michigan"],


    "University of Michigan - Ann Arbor": ["University MichiganAnn Arbor", "University Michigan Ann Arbor"],


    "Michigan State University": ["Michigan State University"],
    
    
    
    
    # Illinois
    
    
    
    "University Illinois" : ["University Illinois"],


    "University Illinois - Urbana": ["University Illinois UrbanaChamp", "University IllinoisUrbanaChampaig", 
                                     "University IllinoisUrbana", "University IllinoisUrbanaChampaigne", 
                                     "University Illinois UrbanaChampaign", "University Illinois Urbana", 
                                     "University IllinoisUrbanaChampaign", "University ofUlinois UrbanaChampaign",
                                     "University ofRlinois UrbanaChampaign", "University ofRlinois Urbana Champaign", 
                                     "University ofUlinois Urbana Champaign", "University Illinois Urbana Champaigne",
                                     "University Illinois Urbana Champaig", "University Illinois Urbana Champ", 
                                     "University Illinois Urbana Champaign"
                                    ],



    "University of Illinois - Chicago": ["University IllinoisChicago", "University Illinois Chicago"],

    "University Illinois - Chicago Circle": ["University Illinois Chicago Circle", "University IllinoisChicago Circle"],




    "Southern Illinois University": ["Southern Illinois University"],

    "Southern Illinois University - Carbondale":["University Southern Illinois University Carbondale", "Southern Illinois UniversityCarbond", 
                                                  "Southern Illinois University Carbon?ale", "Southern Illinois University Carbondale", 
                                                  "Southern Illinois UniversityCarbondale", "Southern Illinois University Carbond"
                                                ],
    
    
    
    "University of Chicago": ["University Chicago"],
    
    
    "DePaul University": ["DePaul University", "De Paul University"],
    
    "Loyola University": ["Loyola University", "Loyola University Chicago"],
    
    "Northwestern University": ["Northwestern University"],
    
    
    
    
    # Florida
    
    
    "University of Florida": ["University Florida"],

    "University of Florida Gainsville": ["University Florida Gainsville"],


    "Florida State University": ["Florida State University" ],

    "Florida State University - Tallahassee": ["Florida State University Tallahassee"],

    "University of South Florida": ["University South Florida"],

    "University of South Florida - Tampa": ["University South FloridaTampa", "University South Florida Tampa"],

    "University of Miami": ["University Miami"], ##This is not Miami University, OH, but the University of Miami, FL
    
    
    
    
    # Iowa
    
    
    "University of Iowa": ["University Iowa"],
    
    "State University of Iowa": ["State University Iowa"],
    
    
    # Other US states
    
    
    "University of Arizona": ["University Arizona"],

    "University of Arkansas":["University Arkansas"],

    "Brown University": ["Brown University"],

    "University of Kansas": ["University Kansas"],

    "University of Kentucky": ["University Kentucky"],

    "University of Minnesota":["University Minnesota"],

    "University of Nebraska": ["University Nebraska", "Universty Nebraska", "University Nebraska Lincoln", "University NebraskaLincoln"],

    "University of New Mexico": ["University New Mexico"],

    "University Oklahoma": ["University Oklahoma"],

    "University Oklahoma - Norman": ["University OklahomaNorman", "University Oklahoma Norman"],

    "Tulane University":["Tulane University"],

    "University of Utah": ["University Utah"],

    "University of Virginia": ["University Virginia"],

    "University of Washington": ["University Washington", "University Washington Seattle"],
    
    "University of Oregon": ["University Oregon"],
    
    "University of Hawaii":["University Hawaii", "University HawaiiManoa", "University HawaiiMonoa",
                         "University Hawaii Manoa", "University Hawaii Monoa"],
    
    
    
    # Canada
    
    
    "University Alberta": ["University Alberta"],
    
    "University Calgary": ["University Calgary"],

    "Laval University": ["Universit? Laval", "Laval University"],
    
    "University of Montreal": ["University Montr?al", 
                               "Universit? de Montreal", 
                               "Universit? De Montr?al", 
                               "Universit? de Montr?al"
                              ],

    "Univerisity Ottawa": ["University Ottawa"],

    "University of Quebec - TR": ["Universit? du Qu?bec? Trois Rivi?res", 
                                  "Universit? du Qu?bec? T roisRivi?res", 
                                  "Universit? du Qu?bec? TroisRiv?res", 
                                  "Universit? de Qu?bec a TroisRivi?res",
                                  "Universit? du Qu?bec? T rois Rivi?res",
                                  "Universit? de Qu?bec a Trois Rivi?res",
                                  "Universit? du Qu?bec? Trois Riv?res"
                                 ],
    "Ontario Institute for Studies in Education": ["Ontario Institute for Studies in Education"],

    "University Western Ontario":["University Western Ontario"],

    "University Toronto": ["University Toronto"],

    "University of Waterloo": ["University Waterloo"],

    "University of British Columbia": ["University British Columbia"],
    
    "McGill University": ["McGill University"],
    
    "McMaster University":["McMaster University"],
    
    "University of Guelph": ["University Guelph", "University ofGuelph"],
    "Queen-s University": ["Queens University", "Queens University Ontario", "Queenys University"],
    
    "York University": ["York University"],
    
    
}

# conversion to direct mapping in order to use dictionary with the replace() method
direct_mapping_universities_spelling={
    spelling_variant : normalized_name
    for normalized_name, spelling_variants in inverted_mapping_universities_spelling.items()
    for spelling_variant in spelling_variants
}

