#!/usr/bin/env python3
"""
Add contextual inline links to 22 location SEO pages.
Strictly verifies each text string exists in the body before modifying.
"""

import os, re, sys

DIR = '/workspaces/blogger-theme/docs/blog-templates'

def get_body_bounds(content):
    faq_idx = content.find('<h2>Frequently Asked Questions</h2>')
    if faq_idx == -1: faq_idx = len(content)
    byline_end = content.find('</div>', content.find('Published'))
    if byline_end == -1: byline_end = 0
    body_start = content.find('<p>', byline_end)
    if body_start == -1: body_start = 0
    return body_start, faq_idx

def count_in_body(content):
    bs, fi = get_body_bounds(content)
    return len(re.findall(r'href=["\']/', content[bs:fi]))

# Build verified edits: each entry is (filename, [(needle, replacement)])
# I verify every needle against the actual file before including it.
# For FAQ-only text, I find alternative body text.

EDITS = {}

# ============ USA ============
EDITS['seo-services-usa.html'] = [
    ('<strong>Local SEO for US Cities</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for US Cities</a></strong>'),
    ('From technical SEO to content to link building', 'From <a href="/2026/06/technical-seo-services.html">technical SEO</a> to content to link building'),
    ('SEO services in the USA</strong> from RankrSEO help businesses across all 50 states', '<a href="/2026/06/seo-company-services.html">SEO company services in the USA</a> help businesses across all 50 states'),
    ('trillions of Google searches annually.', 'trillions of Google searches annually, requiring <a href="/2026/06/seo-audit-services.html">comprehensive SEO audit services</a>.'),
]

# ============ UK ============
EDITS['seo-services-uk.html'] = [
    ('<strong>Local SEO for UK Cities</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for UK Cities</a></strong>'),
    ('<strong>Voice Search Optimization</strong>', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> and <strong>Voice Search Optimization</strong>'),
    ('British English, cultural context, and market-specific', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> with British English, cultural context, and market-specific'),
    ('in London, Manchester, Birmingham, Edinburgh', 'in <a href="/2026/06/seo-services-london.html">London</a>, Manchester, Birmingham, Edinburgh'),
    ('UK consumers trust organic results more than paid ads', '<a href="/2026/06/seo-company-services.html">SEO company services in the UK</a> help British consumers who trust organic results more than paid ads'),
]

# ============ INDIA ============
EDITS['seo-services-india.html'] = [
    ('<strong>Local SEO for Indian Cities</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Indian Cities</a></strong>'),
    ('<strong>Technical SEO</strong> \u2014 Core Web Vitals', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> \u2014 Core Web Vitals'),
    ('Delhi, Mumbai, Bangalore, Hyderabad, Chennai, Pune, Kolkata', '<a href="/2026/06/seo-services-delhi.html">Delhi</a>, Mumbai, Bangalore, Hyderabad, Chennai, Pune, Kolkata'),
    ('<strong>Cost-Effective Solutions</strong>', '<strong><a href="/2026/06/affordable-seo-services.html">Affordable SEO Services</a></strong>'),
    ('helping you dominate search results both in India and globally', '<a href="/2026/06/seo-company-services.html">SEO company services in India</a> helping you dominate search results both in India and globally'),
]

# ============ CANADA ============
EDITS['seo-services-canada.html'] = [
    ('<strong>Local SEO for Canadian Cities</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Canadian Cities</a></strong>'),
    ('<strong>Bilingual SEO (EN/FR)</strong>', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> and <strong>Bilingual SEO (EN/FR)</strong>'),
    ('SEO services in Canada</strong> from RankrSEO help Canadian businesses rank nationwide', '<a href="/2026/06/seo-company-services.html">SEO company services in Canada</a> help Canadian businesses rank nationwide'),
    ('Toronto, Vancouver, Montreal, Calgary, Edmonton, Ottawa, Winnipeg', '<a href="/2026/06/seo-services-toronto.html">Toronto</a>, Vancouver, Montreal, Calgary, Edmonton, Ottawa, Winnipeg'),
    ("businesses need SEO that works in both English and French", 'businesses need <a href="/2026/06/affordable-seo-services.html">affordable SEO services</a> that work in both English and French'),
]

# ============ AUSTRALIA ============
EDITS['seo-services-australia.html'] = [
    ('<strong>Local SEO for Australian Cities</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Australian Cities</a></strong>'),
    ('Aussie businesses are investing heavily', '<a href="/2026/06/seo-services-sydney.html">businesses in Sydney</a> and across Australia are investing heavily'),
    ('SEO is the most cost-effective growth channel available', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> are the most cost-effective growth channel available'),
    ('Sydney, Melbourne, Brisbane, Perth, Adelaide, Gold Coast', '<a href="/2026/06/seo-services-sydney.html">Sydney</a>, Melbourne, Brisbane, Perth, Adelaide, Gold Coast'),
    ('Australian consumers conduct over 6 billion Google searches each year.', 'Australian consumers conduct over 6 billion Google searches each year, requiring <a href="/2026/06/seo-audit-services.html">strategic SEO audit services</a>.'),
]

# ============ DELHI ============
EDITS['seo-services-delhi.html'] = [
    ('help businesses across Delhi', '<a href="/2026/06/seo-company-services.html">SEO company services in Delhi</a> help businesses across Delhi'),
    ('<strong>Local SEO for Delhi NCR</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Delhi NCR</a></strong>'),
    ('businesses across Delhi, Gurgaon, Noida', 'businesses across <a href="/2026/06/seo-services-india.html">Delhi</a>, Gurgaon, Noida'),
    ('<strong>Technical SEO</strong> \u2014 Page speed', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> \u2014 Page speed'),
    ('Delhi NCR-focused strategy', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> with a Delhi NCR-focused strategy'),
]

# ============ BANGALORE ============
EDITS['seo-services-bangalore.html'] = [
    ('help brands in the Garden City capture high-intent traffic', '<a href="/2026/06/seo-company-services.html">SEO company services in Bangalore</a> help brands in the Garden City capture high-intent traffic'),
    ('<strong>Local SEO for Bangalore</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Bangalore</a></strong>'),
    ('<strong>Technical SEO</strong> \u2014 Comprehensive technical audits', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> \u2014 Comprehensive technical audits'),
    ('startup ecosystem with scalable strategies', 'startup ecosystem with <a href="/2026/06/affordable-seo-services.html">affordable SEO services</a> and scalable strategies'),
    ('SEO services in Bangalore</strong> from RankrSEO help brands in the Garden City capture high-intent traffic and grow revenue',
     '<a href="/2026/06/seo-services-india.html">SEO services across India</a> \u2014 our Bangalore services help brands in the Garden City capture high-intent traffic and grow revenue'),
]

# ============ MUMBAI ============
EDITS['seo-services-mumbai.html'] = [
    ('help local businesses dominate search results and attract quality leads.', '<a href="/2026/06/seo-company-services.html">SEO company services in Mumbai</a> help local businesses dominate search results and attract quality leads.'),
    ('<strong>Local SEO for Mumbai</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Mumbai</a></strong>'),
    ('On-page and technical SEO tailored for Mumbai businesses', '<a href="/2026/06/technical-seo-services.html">Technical SEO</a> and on-page optimization tailored for Mumbai businesses'),
    ('most cost-effective way to grow your business in this competitive city', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> as the most cost-effective way to grow'),
    ('Mumbai SEO packages start from \u20b915,000', '<a href="/2026/06/seo-services-delhi.html">SEO in Delhi</a> and Mumbai \u2014 our Mumbai packages start from \u20b915,000'),
]

# ============ CHENNAI ============
EDITS['seo-services-chennai.html'] = [
    ('drive tangible results for local enterprises.', '<a href="/2026/06/seo-company-services.html">SEO company services in Chennai</a> drive tangible results for local enterprises.'),
    ('<strong>Local SEO for Chennai</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Chennai</a></strong>'),
    ('comprehensive technical audit focused on mobile', '<a href="/2026/06/technical-seo-services.html">technical SEO audit</a> focused on mobile'),
    ('English and Tamil search queries to capture the full audience', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> for English and Tamil search queries'),
    ("Chennai's digital economy is accelerating rapidly", '<a href="/2026/06/seo-services-india.html">SEO services across India</a> \u2014 Chennai\u2019s digital economy'),
]

# ============ HYDERABAD ============
EDITS['seo-services-hyderabad.html'] = [
    ('deliver measurable results for businesses across the city.', '<a href="/2026/06/seo-company-services.html">SEO company services in Hyderabad</a> deliver measurable results for businesses across the city.'),
    ('<strong>Local SEO for Hyderabad</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Hyderabad</a></strong>'),
    ('<strong>IT & Pharma SEO</strong>', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> and <strong>IT & Pharma SEO</strong>'),
    ('SEO has become essential for local brands to capture online attention', '<a href="/2026/06/seo-services-bangalore.html">SEO in Bangalore</a> and Hyderabad \u2014 SEO is essential for local brands'),
    ('Consistent top rankings for Hyderabad clients', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> with consistent top rankings for Hyderabad clients'),
]

# ============ KOLKATA ============
EDITS['seo-services-kolkata.html'] = [
    ('help local brands capture high-intent traffic and grow online.', '<a href="/2026/06/seo-company-services.html">SEO company services in Kolkata</a> help local brands capture high-intent traffic and grow online.'),
    ('<strong>Local SEO for Kolkata</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Kolkata</a></strong>'),
    ('<strong>IT & BPO SEO</strong>', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> and <strong>IT & BPO SEO</strong>'),
    ('Cost-effective SEO solutions designed for Kolkata', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> designed for Kolkata'),
    ('Bengali and English SEO services to help you connect', '<a href="/2026/06/seo-services-india.html">SEO services in India</a> \u2014 Bengali and English SEO services'),
]

# ============ PUNE ============
EDITS['seo-services-pune.html'] = [
    ('help local businesses attract more customers through organic search.', '<a href="/2026/06/seo-company-services.html">SEO company services in Pune</a> help local businesses attract more customers through organic search.'),
    ('<strong>Local SEO for Pune</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Pune</a></strong>'),
    ('<strong>Technical SEO & Audits</strong>', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a> & Audits</strong>'),
    ('Our Pune SEO packages start from', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> \u2014 our Pune packages start from'),
    ('Pune\'s population of over 7 million includes', '<a href="/2026/06/seo-services-mumbai.html">SEO services in Mumbai</a> and Pune serve a combined metro population'),
]

# ============ LONDON ============
EDITS['seo-services-london.html'] = [
    ('help businesses across the capital', '<a href="/2026/06/seo-company-services.html">SEO company services in London</a> help businesses across the capital'),
    ('<strong>Local SEO for London</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for London</a></strong>'),
    ('<strong>Technical SEO</strong> \u2014 Core Web Vitals', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> \u2014 Core Web Vitals'),
    ('We offer specialised SEO packages for London startups', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> \u2014 we offer specialised packages for London startups'),
    ('London is one of the most competitive digital markets', '<a href="/2026/06/seo-services-uk.html">SEO services in the UK</a> \u2014 London is one of the most competitive digital markets'),
]

# ============ MANCHESTER ============
EDITS['seo-services-manchester.html'] = [
    ('help local brands achieve top Google rankings.', '<a href="/2026/06/seo-company-services.html">SEO company services in Manchester</a> help local brands achieve top Google rankings.'),
    ('<strong>Local SEO for Manchester</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Manchester</a></strong>'),
    ('<strong>AI SEO / GEO</strong>', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> and <strong>AI SEO / GEO</strong>'),
    ('2.8 million residents generate millions of local searches', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> for Manchester\u2019s 2.8 million residents who generate millions of local searches'),
    ('Manchester SEO packages start from \u00a31,000', '<a href="/2026/06/seo-services-london.html">SEO in London</a> and Manchester \u2014 our packages start from \u00a31,000'),
]

# ============ BIRMINGHAM ============
EDITS['seo-services-birmingham.html'] = [
    ('deliver results that drive real growth.', '<a href="/2026/06/seo-company-services.html">SEO company services in Birmingham</a> deliver results that drive real growth.'),
    ('<strong>Local SEO for Birmingham</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Birmingham</a></strong>'),
    ('<strong>Manufacturing & Industrial SEO</strong>', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> and <strong>Manufacturing & Industrial SEO</strong>'),
    ("Birmingham's 1.1 million residents", '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> for Birmingham\'s 1.1 million residents'),
    ('making SEO a vital investment for local businesses', 'Like <a href="/2026/06/seo-services-manchester.html">SEO in Manchester</a>, making SEO a vital investment for local businesses'),
]

# ============ NEW YORK ============
EDITS['seo-services-new-york.html'] = [
    ('help NYC businesses', '<a href="/2026/06/seo-company-services.html">SEO company services in New York</a> help NYC businesses'),
    ('<strong>Local SEO for NYC Boroughs</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for NYC Boroughs</a></strong>'),
    ('<strong>Enterprise SEO</strong>', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> and <strong>Enterprise SEO</strong>'),
    ('200,000 businesses in Manhattan alone', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> for NYC\u2019s 200,000 businesses in Manhattan alone'),
    ('Silicon Alley', '<a href="/2026/06/seo-services-san-francisco.html">SEO in San Francisco</a> and NYC\u2019s Silicon Alley'),
]

# ============ CHICAGO ============
EDITS['seo-services-chicago.html'] = [
    ('deliver results that matter.', '<a href="/2026/06/seo-company-services.html">SEO company services in Chicago</a> deliver results that matter.'),
    ('<strong>Local SEO for Chicago</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Chicago</a></strong>'),
    ("Chicago's mobile-first audience demands pristine Core Web Vitals", '<a href="/2026/06/technical-seo-services.html">Technical SEO</a> for Chicago\u2019s mobile-first audience demands pristine Core Web Vitals'),
    ('Our Chicago SEO packages start from', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> \u2014 our Chicago packages start from'),
    ('Without strong SEO, your Chicago business is invisible', '<a href="/2026/06/seo-services-new-york.html">SEO in New York</a> and Chicago \u2014 without strong SEO, your business is invisible'),
]

# ============ LOS ANGELES ============
EDITS['seo-services-los-angeles.html'] = [
    ('help LA brands dominate local search results.', '<a href="/2026/06/seo-company-services.html">SEO company services in Los Angeles</a> help LA brands dominate local search results.'),
    ('<strong>Local SEO for LA</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for LA</a></strong>'),
    ('<strong>AI SEO / GEO</strong>', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> and <strong>AI SEO / GEO</strong>'),
    ('Our LA SEO packages start from', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> \u2014 our LA packages start from'),
    ('In a city as competitive as LA, ranking on page one is a must', '<a href="/2026/06/seo-services-san-francisco.html">SEO in San Francisco</a> and LA \u2014 in a city as competitive as LA, ranking is a must'),
]

# ============ SAN FRANCISCO ============
EDITS['seo-services-san-francisco.html'] = [
    ('help Bay Area companies dominate search.', '<a href="/2026/06/seo-company-services.html">SEO company services in San Francisco</a> help Bay Area companies dominate search.'),
    ('<strong>Local SEO for SF</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for SF</a></strong>'),
    ('<strong>Enterprise SEO</strong>', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> and <strong>Enterprise SEO</strong>'),
    ('Our SF SEO packages start from', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> \u2014 our SF packages start from'),
    ('SF businesses require sophisticated SEO strategies', '<a href="/2026/06/seo-services-new-york.html">SEO in New York</a> and SF both require sophisticated SEO strategies'),
]

# ============ TORONTO ============
EDITS['seo-services-toronto.html'] = [
    ('help local businesses dominate search and attract quality leads.', '<a href="/2026/06/seo-company-services.html">SEO company services in Toronto</a> help local businesses dominate search and attract quality leads.'),
    ('<strong>Local SEO for Toronto</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Toronto</a></strong>'),
    ('<strong>AI SEO / GEO</strong>', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> and <strong>AI SEO / GEO</strong>'),
    ('Our Toronto SEO packages start from', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> \u2014 our Toronto packages start from'),
    ('strong SEO directly impacts your bottom line', '<a href="/2026/06/seo-services-canada.html">SEO services in Canada</a> \u2014 strong SEO directly impacts your bottom line'),
]

# ============ SYDNEY ============
EDITS['seo-services-sydney.html'] = [
    ('help local businesses achieve top rankings and attract quality leads.', '<a href="/2026/06/seo-company-services.html">SEO company services in Sydney</a> help local businesses achieve top rankings and attract quality leads.'),
    ('<strong>Local SEO for Sydney</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Sydney</a></strong>'),
    ('<strong>Financial Services SEO</strong>', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> and <strong>Financial Services SEO</strong>'),
    ('Our Sydney SEO packages start from', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> \u2014 our Sydney packages start from'),
    ('SEO is essential for any Sydney business', '<a href="/2026/06/seo-services-melbourne.html">SEO in Melbourne</a> and Sydney \u2014 SEO is essential for any Sydney business'),
]

# ============ MELBOURNE ============
EDITS['seo-services-melbourne.html'] = [
    ('help local brands cut through the noise and capture high-intent traffic.', '<a href="/2026/06/seo-company-services.html">SEO company services in Melbourne</a> help local brands cut through the noise and capture high-intent traffic.'),
    ('<strong>Local SEO for Melbourne</strong>', '<strong><a href="/2026/06/local-seo-services.html">Local SEO for Melbourne</a></strong>'),
    ('<strong>Retail & Ecommerce SEO</strong>', '<strong><a href="/2026/06/technical-seo-services.html">Technical SEO</a></strong> and <strong>Retail & Ecommerce SEO</strong>'),
    ('Our Melbourne SEO packages start from', '<a href="/2026/06/affordable-seo-services.html">Affordable SEO services</a> \u2014 our Melbourne packages start from'),
    ('strong SEO is the difference between being found and being forgotten', '<a href="/2026/06/seo-services-sydney.html">SEO in Sydney</a> and Melbourne \u2014 strong SEO is the difference between being found and being forgotten'),
]


def verify_all():
    """Verify all needles exist in body before running."""
    all_ok = True
    for filename in sorted(EDITS.keys()):
        filepath = os.path.join(DIR, filename)
        with open(filepath) as f:
            content = f.read()
        bs, fi = get_body_bounds(content)
        body = content[bs:fi]
        
        for i, (needle, _) in enumerate(EDITS[filename]):
            if needle not in body:
                fc = content.count(needle)
                print(f"PRE-FAIL: {filename}[{i}] body=False file={fc}")
                print(f"  Needle: \"{needle[:70]}\"")
                all_ok = False
    return all_ok


def main():
    verify_all()
    # Continue even if some fail - we skip those edits
    print("\nApplying edits (skipping failures)...\n")
    
    results = []
    for filename in sorted(EDITS.keys()):
        filepath = os.path.join(DIR, filename)
        with open(filepath) as f:
            content = f.read()
        
        old_count = count_in_body(content)
        bs, fi = get_body_bounds(content)
        
        before = content[:bs]
        body = content[bs:fi]
        after = content[fi:]
        
        for needle, replacement in EDITS[filename]:
            if needle not in body:
                print(f"  SKIP: '{needle[:60]}' not in body (in FAQ or missing)")
                continue
            body = body.replace(needle, replacement, 1)
        
        new_content = before + body + after
        with open(filepath, 'w') as f:
            f.write(new_content)
        
        new_count = count_in_body(new_content)
        results.append((filename, old_count, new_count, new_count - old_count))
        print(f"{filename}: {old_count} \u2192 {new_count} links (+{new_count-old_count})")
    
    print("\n" + "="*80)
    print(f"{'File':50s} {'Old':>5s} {'New':>5s} {'Added':>5s}")
    print("="*80)
    to, tn = 0, 0
    for fname, old, new_, added in results:
        print(f"{fname:50s} {old:5d} {new_:5d} {added:5d}")
        to += old; tn += new_
    print("="*80)
    print(f"{'TOTAL':50s} {to:5d} {tn:5d} {tn-to:5d}")

if __name__ == '__main__':
    main()
