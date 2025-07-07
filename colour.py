import re
from collections import defaultdict

# Example cleaned passage
text = re.sub(r'[^A-Z]', '', """
IM A SHELL OF MYSELF - I TRY TO WRITE SOMETHING SO PROFOUND THAT IT WILL BEAT THE IRONY EPIDEMIC, THE ARTIST'S BREIFS YOU IGNORE AND THE CAPTION THAT IS AI GENERATED. 
IM IN THE LOOP OF WANTING TO REACH GREATNESS WITH NO MEANS. NO WAY TO GET THERE, BUT IM TOO LAZY TO MAKE MY PATH. 
DO I FALL VICTIM TO THE LACK OF "GRINDSET", BUT NO. I WIAS TOLD IT WAS MADE TO MAKE MILLIONS OFF PEOPLE'S WILLINGBNESS TO MAKE IT BIG. 
BUT I WANT TO WRITE SOMETHING SO PROFOUND. 
DO I SAY SOMETHING CONTROVERSIAL THAT I DONT KNOW THE MEANING, BUT I MAKE EVERYONE AROUND ME TRY TO MAKE MEANING FROM IT. 
DO YOU THINK EVERYTHING I DO MAKES FOR A STORY FOR MY FANS WILL SHARE. WILL I EVER HAVE FANS? WHY WOULD THEY LIKE ME? 
I WONDER IF I WILL EVER MAKE A PIECE OF MEDIA SO PROFOUND, IF I EVER GO INTO HIDING, THEY WILL STILL LOVE ME? 
I WONDER WHAT THAT ADMIRATION WILL FEEL LIKE? 
I WONDER IF EVER TO STICK TO A PROJECT LONG ENOUGH, TO RELEASE TO WARRANT SUCH A THING. 
I FEEL MYSELF. RIGHT NOW. BE UNSURE WITH WHAT IM SAYING. AS I THINK MORE AND MORE. 
I GROW LESS IN MY WORDS, MY WRITING, MY CONVICTION AND MY GOAL. I CANT EVEN HAVE A CLEAR IMAGE OF STABLE MUNDANE. 
SO I STRIVE FOR INCREDIBLE FAME, TO OFFSET THE FACT I CANT FIGURE OUT THE NORMACALLY OF LIVING. 
BEING ABLE TO DO SUCH A THING MY GOAL, I GUESS. I DECIDED RIGHT NOW. YEAH. LIFE DOES NOT HAVE TO BE HARD. 
MIDST PEOPLE NEVER CREATE ANYTHING MEANINGFUL. AND I THINK THATS FINE. I KNOW MY STATEMENT IS NOT PROFOUND. 
I GUESS I NEEDED THIS TO GET THERE MYSELF. 
I THINK OF MYSELF NOW. I WANT TO BE CONSCIENTIOUSNESS OF MY LIFE CAN BE WITH THE CHOICES I MAKE. 
TO MAKE SURE I HAVE FULFILLMENT IN THE COMFORT WHERE I AM. AT ANY TIME. ANY WHERE. 
WITH THE PEOPLE AROUND ME. TO SHARE WITH OUT BEING ATTACKED. AND BE LIFTED TO REACH MY POTENITAL. 
""".upper())

# Pre-collected top n-grams with freq ≥ 5
top_grams = {
    6: ["TOMAKE"],
    5: ["THING", "OMAKE", "TOMAK"],
    4: ["THIN", "MAKE", "HING", "WILL", "EVER", "OUND", "OMAK", "THAT", "TTHE", "WITH", "MEAN", "TOMA"],
    3: ["ING", "THE", "THI", "HIN", "ILL", "HAT", "MAK", "AKE", "EAN", "ITH", "VER", "EVE", "UND", "WIL",
        "ETO", "MET", "OUN", "THA", "TTH", "ORE", "REA", "ANT", "ESS", "NOW", "OMA", "MYS", "PRO", "ATI",
        "AND", "WIT", "MEA", "TIM", "TOM", "EME", "EWI"],
    2: ["TH", "IN", "TO", "AN", "TI", "EA", "NG", "RE", "HE", "AT", "IT", "ME", "ND", "HA", "ER", "LL",
        "ET", "NT", "VE", "MA", "OF", "MY", "ES", "WI", "ON", "HI", "OU", "NO", "OR", "KE", "OM", "EI",
        "EL", "RI", "RO", "ST", "LI", "OW", "IL", "EM", "LE", "IM", "SO", "TT", "IF", "IG", "EN", "NE",
        "ED", "AK", "TE", "FO", "UN", "BE", "DE", "AR", "EC", "DI", "EV", "AS", "SE", "FI", "YT", "OP",
        "ID", "IC", "AC", "UT", "DO", "IW", "YS", "LF", "MI", "IS", "WA", "SS", "NS", "OI", "AL", "EO",
        "SI", "DM", "TA", "RY", "PR", "DT", "CT", "CA", "IO", "GE", "CH", "FA", "EW", "EF", "WH", "YW",
        "WO", "FE", "HT"],
    1: ["E", "I", "T", "O", "A", "N", "S", "R", "H", "L", "M", "F", "D", "W", "G", "Y", "C", "U", "K", "B", "V", "P"]
}

# Sort grams by length descending
ordered_grams = []
for n in sorted(top_grams.keys(), reverse=True):
    ordered_grams.extend(top_grams[n])

# Assign each gram a color
color_palette = [
    "#ffadad", "#ffd6a5", "#fdffb6", "#caffbf", "#9bf6ff",
    "#a0c4ff", "#bdb2ff", "#ffc6ff", "#fffffc"
]
gram_colors = {gram: color_palette[i % len(color_palette)] for i, gram in enumerate(ordered_grams)}

# Annotate text with spans
def annotate_html(text, grams):
    i = 0
    result = []
    while i < len(text):
        matched = False
        for gram in grams:
            n = len(gram)
            if text[i:i+n] == gram:
                color = gram_colors[gram]
                result.append(f'<span style="background-color:{color}">{gram}</span>')
                i += n
                matched = True
                break
        if not matched:
            result.append(text[i])
            i += 1
    return ''.join(result)

annotated_html = annotate_html(text, ordered_grams)

# Wrap in HTML template
html_output = f"""
<html>
<head><meta charset="UTF-8"><title>Highlighted Grams</title></head>
<body style="font-family:monospace; line-height:1.5;">
<p>{annotated_html}</p>
</body>
</html>
"""

# Save to file
with open("highlighted_ngrams.html", "w", encoding="utf-8") as f:
    f.write(html_output)
