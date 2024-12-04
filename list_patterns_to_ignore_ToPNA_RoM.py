#!/usr/bin/env python
# coding: utf-8

# In[ ]:


patterns = ['DOCTORAL DISSERTATIONS', 'This content downloaded from', 'All use subject to', "The three figures below each institution", 'graduate students enro','ed in its philosophy department', '(2) the number ', 'to (1) the numb', '(3) the number', 'of faculty members', 'residence graduate students', 'his information is included also for', 'dash indicates that the inform', 'required has not been provid', 'faculty members teaching in the grad', 'The Review of Metaphysics', 'full time students as that term','students as that term', 'present list may not be complete', 'some of the institutions which confer doctoral', 'in part because some of the institutions', 'our requests for information may have conferred', 'basis of written dissertaions. We hope', 'when we plan to publish the', 'dissertations in philosophy in the two', r'\A\s*Metaphysics\s*\.*\n', 'Review of Metaphysics', 'SURVEY OF GRADUATE PROGRAMS', 'North America. We wish to thank', r'represented for their cooperation.\n', r'\d\d\d\.\d\d\.\d\d\d\.\d\d\d', r'\d\d:\d\d:\d\d\s\+', 'fifteen members teach courses in their', r'\Aments.\s*\n', r'\A\s*\*\s*\w', 'Holyoke Colleges, and this last', 'faculty members in the', 'ere information was not supplied', 'Review invites and encourages', 'recently begun a Doctoral Program or', 'one in the near future', 'the graduate program', r'\A\sprogram\.*', 'program\.\n' 'graduate students as the term', ' Mount Holyoke and Smith', '\D\d\d\d\n', 'SUR VEY OF GRADUA TE PROGRAMS', 'graduate students as the term is understood by the institution', 'students as the term is understood', 'graduate program', ' and (3) the', 'received too late to be included','various dissertation committees to name']


#patterns results from the enumeration of recurring elements of lines that need to be ignored, e.g. headers,footnotes, editors' stamps, page numbers and so on. patterns and string are isolated by manual browsing and successive additions

