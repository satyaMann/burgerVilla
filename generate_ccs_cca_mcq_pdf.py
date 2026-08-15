from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
)


OUTPUT = Path(__file__).with_name(
    "CCS_CCA_Rules_1965_100_UPSC_Style_MCQs.pdf"
)

TWO_OPTIONS = [
    "1 only",
    "2 only",
    "Both 1 and 2",
    "Neither 1 nor 2",
]

questions = []


def add2(section, statement_1, statement_2, answer):
    questions.append(
        {
            "section": section,
            "statements": [statement_1, statement_2],
            "options": TWO_OPTIONS,
            "answer": answer,
        }
    )


def add3(section, statements, options, answer):
    questions.append(
        {
            "section": section,
            "statements": statements,
            "options": options,
            "answer": answer,
        }
    )


general = "General provisions and classification"
add2(
    general,
    "These rules are called the CCS (Classification, Control and Appeal) Rules, 1965.",
    "They came into force on 1 December 1965.",
    "C",
)
add2(
    general,
    "These rules were framed under the proviso to Article 309 and clause (5) of Article 148.",
    '"Commission" under these rules means the Central Vigilance Commission.',
    "A",
)
add2(
    general,
    '"Service" means a civil service of a State.',
    '"Disciplinary authority" means an authority competent to impose a Rule 11 penalty.',
    "B",
)
add2(
    general,
    "These rules ordinarily apply to members of the All India Services.",
    "These rules ordinarily apply to persons in casual employment.",
    "D",
)
add2(
    general,
    "Civilian Government servants in Defence Services are generally covered by these rules.",
    "The President may exclude a group of Government servants from all or some of these rules.",
    "C",
)
add2(
    general,
    "Railway servants are ordinarily excluded from these rules.",
    "Doubts regarding the application of these rules are finally decided by UPSC.",
    "A",
)
add2(
    general,
    'A State Government employee deputed to the Central Government is excluded from "Government servant."',
    'An employee of a local authority deputed to the Central Government is included in "Government servant."',
    "B",
)
add2(
    general,
    '"Head of Department" means an authority declared as such under the General Financial Rules.',
    '"Head of Office" means an authority declared as such under the Civil Service Regulations.',
    "D",
)
add2(
    general,
    "Civil Services of the Union are classified into Groups A, B, C and D under the bare rules.",
    "Different grades of the same Service may be placed in different groups.",
    "C",
)
add3(
    general,
    [
        "Class I corresponds to Group A.",
        "Class II corresponds to Group B.",
        "Class III corresponds to Group B.",
    ],
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    "A",
)
add2(
    general,
    "Services constituting each group are determined solely by UPSC.",
    "Services and grades constituting each group are specified in the Schedule.",
    "B",
)
add2(
    general,
    "A Central Civil post not included in another Service is excluded from the General Central Service.",
    "Its holder becomes a General Central Service member even if already a member of another Central Civil Service of the same group.",
    "D",
)
add2(
    general,
    "Group A appointments are ordinarily made by the President.",
    "The President may delegate this power by a general or special order.",
    "C",
)
add2(
    general,
    "Appointments to Groups B, C and D Services other than the General Central Service are made by authorities specified in the Schedule.",
    "Every Group A appointment must be made by UPSC.",
    "A",
)
add2(
    general,
    "Appointments to General Central Service posts in Groups B, C and D must always be made personally by the President.",
    "If no presidential order exists, appointments are made by authorities specified in the Schedule.",
    "B",
)
add2(
    general,
    "The President cannot delegate the power to make Group A appointments.",
    "Rule 9 deals exclusively with Group A appointments.",
    "D",
)

suspension = "Suspension"
add2(
    suspension,
    "Suspension may be ordered when disciplinary proceedings are contemplated or pending.",
    "Suspension may be ordered when a criminal case is under investigation, inquiry or trial.",
    "C",
)
add2(
    suspension,
    "Activities prejudicial to State security can be a ground for suspension.",
    "Such activities automatically result in deemed suspension without an order.",
    "A",
)
add2(
    suspension,
    "Detention for exactly 48 hours results in deemed suspension.",
    "Detention exceeding 48 hours results in deemed suspension from the date of detention.",
    "B",
)
add3(
    suspension,
    [
        "Detention for exactly 48 hours results in deemed suspension.",
        "Detention exceeding 48 hours results in deemed suspension.",
        "Such deemed suspension takes effect from the date of detention.",
    ],
    ["1 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    "B",
)
add2(
    suspension,
    "The 48-hour period after conviction runs from the commencement of imprisonment.",
    "Intermittent periods of imprisonment are included.",
    "C",
)
add2(
    suspension,
    "An authority below the appointing authority must report the circumstances of suspension forthwith.",
    "It must always obtain prior approval before ordering suspension.",
    "A",
)
add2(
    suspension,
    "The first suspension review may validly be conducted after 90 days.",
    "Suspension is reviewed on the recommendation of a Review Committee.",
    "B",
)
add2(
    suspension,
    "Suspension may be extended for 365 days at a time.",
    "No subsequent review is required after the first review.",
    "D",
)
add2(
    suspension,
    "Review at 90 days is unnecessary if the employee continues in detention.",
    "After release, the period runs from the later of release or intimation of release.",
    "C",
)
add2(
    suspension,
    "Subject to Rule 10(7), suspension continues until modified or revoked.",
    "Only the original suspending authority can revoke it.",
    "A",
)
add2(
    suspension,
    "Another proceeding automatically extends an existing suspension.",
    "Continuation may be directed for reasons recorded in writing.",
    "B",
)
add2(
    suspension,
    "Further inquiry can always be ordered after a court decides the case on merits.",
    "Deemed suspension then begins from the date further inquiry is ordered.",
    "D",
)
add2(
    suspension,
    "If dismissal is set aside and the case remitted, suspension is deemed to continue from the original dismissal date.",
    "It remains effective until further orders, subject to review provisions.",
    "C",
)
add3(
    suspension,
    [
        "The appointing authority may order suspension.",
        "An authority subordinate to the appointing authority may order suspension.",
        "Only the President personally may revoke suspension.",
    ],
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    "A",
)

penalties = "Penalties and disciplinary authorities"
add2(
    penalties,
    "Censure is a major penalty.",
    "Withholding promotion is a minor penalty.",
    "B",
)
add2(
    penalties,
    "Dismissal is a minor penalty.",
    "Removal is not a Rule 11 penalty.",
    "D",
)
add2(
    penalties,
    "Recovery of pecuniary loss caused by negligence is a minor penalty.",
    "Withholding increments is a minor penalty.",
    "C",
)
add2(
    penalties,
    "Reduction by one stage for up to three years without cumulative effect or pension impact is a minor penalty.",
    "Every reduction to a lower stage is a minor penalty.",
    "A",
)
add2(
    penalties,
    "Compulsory retirement imposed as a penalty is a minor penalty.",
    "Compulsory retirement imposed as a penalty is a major penalty.",
    "B",
)
add2(
    penalties,
    "Removal ordinarily disqualifies future Government employment.",
    "Dismissal can never disqualify future Government employment.",
    "D",
)
add2(
    penalties,
    "Removal does not disqualify future Government employment.",
    "Dismissal ordinarily disqualifies future Government employment.",
    "C",
)
add2(
    penalties,
    "Proved disproportionate assets ordinarily attract removal or dismissal.",
    "No other penalty can be imposed even in an exceptional case for recorded special reasons.",
    "A",
)
add2(
    penalties,
    "Withholding increments for failing a prescribed examination is a Rule 11 penalty.",
    "Non-promotion after due consideration is not a Rule 11 penalty.",
    "B",
)
add3(
    penalties,
    [
        "Stoppage at the efficiency bar is a minor penalty.",
        "Ordinary retirement on superannuation is a major penalty.",
        "Withholding increments for failing a prescribed examination is a penalty.",
    ],
    ["1 only", "2 only", "3 only", "None of the above"],
    "D",
)
add2(
    penalties,
    "Termination of a probationer according to probation conditions is not a penalty.",
    "Termination under the Temporary Service Rules is not a penalty.",
    "C",
)
add2(
    penalties,
    "Compensation recommended by a sexual-harassment Complaints Committee is not a Rule 11 penalty.",
    "Warning is expressly listed as a statutory minor penalty.",
    "A",
)
add2(
    penalties,
    "The President may impose penalties only on Group A officers.",
    "The President may impose any Rule 11 penalty on any Government servant.",
    "B",
)
add2(
    penalties,
    "Any authority subordinate to the appointing authority may impose dismissal with permission.",
    "The CAG exception permits all major penalties against an IA&AS member.",
    "D",
)
add2(
    penalties,
    "The Director, LBSNAA, may impose censure on a probationer undergoing training.",
    "The Director may impose recovery of pecuniary loss after following Rule 16.",
    "C",
)
add2(
    penalties,
    "A person promoted to the next higher group is deemed to belong to that group for Rule 12.",
    "This applies only to substantive promotions.",
    "A",
)
add2(
    penalties,
    "A minor-penalty authority cannot initiate major-penalty proceedings.",
    "It may initiate such proceedings even though it cannot impose the resulting major penalty.",
    "B",
)
add2(
    penalties,
    "A minor-penalty authority is prohibited from initiating major-penalty proceedings.",
    "Only the appointing authority may institute disciplinary proceedings.",
    "D",
)
add2(
    penalties,
    "The highest authority listed in Rule 2(a) is treated as the appointing authority.",
    "A disciplinary authority is competent to impose a Rule 11 penalty.",
    "C",
)
add3(
    penalties,
    [
        "The President may institute disciplinary proceedings.",
        "An authority empowered by the President may institute proceedings.",
        "UPSC may independently institute proceedings under Rule 13.",
    ],
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    "A",
)

inquiry = "Major-penalty inquiry"
add2(
    inquiry,
    "Rule 14 principally prescribes minor-penalty procedure.",
    "Rules 14 and 15 principally govern major-penalty proceedings.",
    "B",
)
add2(
    inquiry,
    "Every major-penalty inquiry must be held under the Public Servants (Inquiries) Act, 1850.",
    "Rule 14 inquiry can never be dispensed with under Rule 19.",
    "D",
)
add2(
    inquiry,
    "The disciplinary authority may itself conduct an inquiry.",
    "A sexual-harassment Complaints Committee is deemed to be the inquiring authority.",
    "C",
)
add2(
    inquiry,
    "Imputations must be framed into definite and distinct articles of charge.",
    "A charge sheet must specify the proposed punishment.",
    "A",
)
add2(
    inquiry,
    "The statement of imputations must exclude an employee's admissions.",
    "It must include lists of relied-upon documents and witnesses.",
    "B",
)
add2(
    inquiry,
    "The initial period for filing a written defence is 30 days.",
    "The maximum total period is 30 days.",
    "D",
)
add2(
    inquiry,
    "Each extension for filing the defence cannot exceed 15 days at a time.",
    "The total period cannot exceed 45 days from receipt of charges.",
    "C",
)
add2(
    inquiry,
    "A Government servant or legal practitioner may be appointed as Presenting Officer.",
    "A Presenting Officer may be appointed only when the disciplinary authority is not conducting the inquiry.",
    "A",
)
add2(
    inquiry,
    "The ten-working-day period runs from receipt of charges by the employee.",
    "It runs from receipt of charge documents by the inquiring authority.",
    "B",
)
add3(
    inquiry,
    [
        "Appearance must ordinarily be fixed within ten working days of the inquiring authority receiving the charge documents.",
        "Additional time cannot exceed ten days.",
        "Filing a written defence automatically dispenses with appearance.",
    ],
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    "A",
)
add2(
    inquiry,
    "A serving employee at the headquarters or inquiry location may act as defence assistant.",
    "A person at another station may be permitted for recorded reasons.",
    "C",
)
add2(
    inquiry,
    "A lawyer may be engaged if the Presenting Officer is a lawyer or permission is granted.",
    "The employee has an unconditional right to engage a lawyer.",
    "A",
)
add2(
    inquiry,
    "An employee may act as defence assistant despite already handling three pending cases.",
    "A retired Government servant may assist subject to prescribed conditions.",
    "B",
)
add2(
    inquiry,
    "A guilty plea need not be signed by the employee.",
    "Full evidence must be taken even on an admitted charge.",
    "D",
)
add2(
    inquiry,
    "If the employee fails to appear, the Presenting Officer may be directed to produce evidence.",
    "The inquiry may be adjourned to a date not exceeding 30 days.",
    "C",
)
add2(
    inquiry,
    "Listed documents may initially be inspected within five days, extendable by five days.",
    "Every Government document must be supplied regardless of relevance.",
    "A",
)
add2(
    inquiry,
    "Witness statements may be supplied only after witnesses are examined.",
    "Requested statements must be supplied at least three days before examination.",
    "B",
)
add2(
    inquiry,
    "Notice for additional documents must be given within 30 days.",
    "The employee need not explain their relevance.",
    "D",
)
add2(
    inquiry,
    "The inquiring authority may refuse irrelevant documents for recorded reasons.",
    "The custodian must produce them or issue a non-availability certificate within one month.",
    "C",
)
add3(
    inquiry,
    [
        "Production may be refused for public-interest or State-security reasons.",
        "Reasons for such refusal must be recorded in writing.",
        "The inquiring authority must continue insisting on production after being informed.",
    ],
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    "A",
)
add2(
    inquiry,
    "The Presenting Officer can never re-examine a witness.",
    "Re-examination on a new matter requires permission of the inquiring authority.",
    "B",
)
add2(
    inquiry,
    "The employee cannot cross-examine departmental witnesses.",
    "The inquiring authority cannot question witnesses.",
    "D",
)
add2(
    inquiry,
    "When new evidence is permitted, three clear days' adjournment may be demanded.",
    "New documents must be made available for inspection before entering the record.",
    "C",
)
add2(
    inquiry,
    "New evidence cannot be introduced merely to fill a gap.",
    "Only the disciplinary authority may call new evidence.",
    "A",
)
add2(
    inquiry,
    "An oral defence need not be recorded.",
    "A copy of the defence statement must be given to the Presenting Officer.",
    "B",
)

special = "Inquiry report and special procedure"
add2(
    special,
    "The disciplinary authority may remit a case for further inquiry for recorded reasons.",
    "An inquiry report must be supplied even when favourable to the employee.",
    "C",
)
add2(
    special,
    "Representation on the inquiry report may be made within 15 days.",
    "A favourable inquiry report need not be supplied.",
    "A",
)
add2(
    special,
    "Commission advice is supplied only after the final order.",
    "The employee may represent against it within 15 days.",
    "B",
)
add2(
    special,
    "The disciplinary authority may ignore the employee's representations.",
    "A separate opportunity against the proposed major penalty is always mandatory.",
    "D",
)
add3(
    special,
    [
        "Minor-penalty proceedings require written communication of the proposed action and imputations.",
        "A Rule 14-type inquiry may be held when considered necessary.",
        "Such inquiry becomes compulsory merely because the employee requests it.",
    ],
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    "A",
)
add2(
    special,
    "Inquiry is mandatory where withholding increments exceeds three years, is cumulative or affects pension.",
    "Full inquiry is mandatory in every minor-penalty case.",
    "A",
)
add2(
    special,
    "An authority competent only to censure all employees may order common proceedings.",
    "If dismissal authorities differ, the highest may order common proceedings with the others' consent.",
    "B",
)
add2(
    special,
    "A common-proceeding order need not identify the disciplinary authority.",
    "Common proceedings must always follow major-penalty procedure.",
    "D",
)
add2(
    special,
    "Rule 19 covers conviction, impracticability of inquiry and State security.",
    "Where required, the Commission must be consulted and representation against its advice permitted.",
    "C",
)
add2(
    special,
    "A borrowing authority may suspend and conduct proceedings against a lent officer.",
    "It may itself impose any major penalty without returning the officer.",
    "A",
)

appeals = "Appeals, revision and review"
add2(
    appeals,
    "No appeal lies against suspension.",
    "No appeal lies against an order made by the President.",
    "B",
)
add2(
    appeals,
    "Every interlocutory order is appealable.",
    "An order passed by an inquiring authority during inquiry is appealable.",
    "D",
)
add2(
    appeals,
    "An appeal lies against suspension.",
    "An appeal lies against imposition or enhancement of a Rule 11 penalty.",
    "C",
)
add2(
    appeals,
    '"Government servant" for Rule 23 includes a person who has ceased to be in service.',
    '"Pension" excludes gratuity and other retirement benefits.',
    "A",
)
add3(
    appeals,
    [
        "A Group A employee's appeal always lies to UPSC.",
        "If the order is made by an authority subordinate to the appointing authority, appeal ordinarily lies to the appointing authority.",
        "In other specified Group A or B cases, appeal may lie to the President.",
    ],
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    "B",
)
add2(
    appeals,
    "An appeal in a common proceeding always lies to the President.",
    "An order made by the President may be appealed to the Union Cabinet.",
    "D",
)
add2(
    appeals,
    "The normal appeal period is 45 days.",
    "Delay may be condoned where sufficient cause is shown.",
    "C",
)
add2(
    appeals,
    "An appeal must be filed separately in the appellant's own name.",
    "Disrespectful language is permitted if allegations are believed to be true.",
    "A",
)
add2(
    appeals,
    "The original authority may wait for directions before forwarding an appeal.",
    "It must forward the appeal, comments and records without avoidable delay.",
    "B",
)
add2(
    appeals,
    "The appellate authority cannot revoke suspension.",
    "In a penalty appeal, it examines only the quantum of penalty.",
    "D",
)
add2(
    appeals,
    "The appellate authority may confirm, enhance, reduce or set aside a penalty.",
    "Enhancement to a major penalty ordinarily requires a Rule 14 inquiry if none was held.",
    "C",
)
add2(
    appeals,
    "The authority that made the original order implements the appellate order.",
    "UPSC implements all appellate orders.",
    "A",
)
add2(
    appeals,
    "Revision may begin before expiry of the appeal period.",
    "An appellate authority may exercise revision within six months.",
    "B",
)
add2(
    appeals,
    "Review under Rule 29-A may be exercised by any disciplinary authority.",
    "Review under Rule 29-A requires no new material or evidence.",
    "D",
)
add3(
    appeals,
    [
        "Orders and notices may be served personally or by registered post.",
        "For sufficient cause, the competent authority may extend time or condone delay unless otherwise expressly provided.",
        "Rule 32 presently contains the operative provision for supplying UPSC advice.",
    ],
    ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
    "A",
)


assert len(questions) == 100, f"Expected 100 questions, found {len(questions)}"


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="DocumentTitle",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=21,
        leading=25,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#17365D"),
        spaceAfter=8 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="Subtitle",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=6 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="Section",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=17,
        textColor=colors.white,
        backColor=colors.HexColor("#2B579A"),
        borderPadding=(5, 7, 5, 7),
        spaceBefore=5 * mm,
        spaceAfter=4 * mm,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        name="Question",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=13,
        textColor=colors.HexColor("#1F2937"),
        spaceAfter=2 * mm,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        name="Statement",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.2,
        leading=12.2,
        leftIndent=5 * mm,
        firstLineIndent=-4 * mm,
        spaceAfter=1.1 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="Prompt",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=8.8,
        leading=11,
        spaceBefore=1 * mm,
        spaceAfter=1.5 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="Option",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=11.5,
        leftIndent=5 * mm,
        spaceAfter=0.6 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="Answer",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9.2,
        leading=12,
        textColor=colors.HexColor("#176B3A"),
        backColor=colors.HexColor("#EAF7EF"),
        borderColor=colors.HexColor("#8BC8A2"),
        borderWidth=0.6,
        borderPadding=(3, 5, 3, 5),
        spaceBefore=2 * mm,
        spaceAfter=4 * mm,
    )
)
styles.add(
    ParagraphStyle(
        name="Source",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8,
        leading=11,
        textColor=colors.HexColor("#4A5568"),
        spaceBefore=4 * mm,
    )
)


def page_decor(canvas, doc):
    canvas.saveState()
    page_width, page_height = A4
    canvas.setStrokeColor(colors.HexColor("#D1D5DB"))
    canvas.setLineWidth(0.5)
    canvas.line(18 * mm, 15 * mm, page_width - 18 * mm, 15 * mm)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(colors.HexColor("#6B7280"))
    canvas.drawString(
        18 * mm,
        10.5 * mm,
        "CCS (CCA) Rules, 1965 - 100 UPSC-Style MCQs",
    )
    canvas.drawRightString(
        page_width - 18 * mm,
        10.5 * mm,
        f"Page {doc.page}",
    )
    canvas.restoreState()


doc = BaseDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    leftMargin=18 * mm,
    rightMargin=18 * mm,
    topMargin=17 * mm,
    bottomMargin=20 * mm,
    title="CCS (CCA) Rules, 1965 - 100 UPSC-Style MCQs",
    author="Prepared from the Department of Personnel and Training bare rules",
    subject="Statement-based multiple-choice questions with answers",
)
frame = Frame(
    doc.leftMargin,
    doc.bottomMargin,
    doc.width,
    doc.height,
    id="main",
)
doc.addPageTemplates(
    [PageTemplate(id="mcq", frames=[frame], onPage=page_decor)]
)

story = [
    Spacer(1, 20 * mm),
    Paragraph(
        "CCS (CCA) Rules, 1965",
        styles["DocumentTitle"],
    ),
    Paragraph(
        "100 UPSC-Style Statement-Based Multiple-Choice Questions",
        styles["Subtitle"],
    ),
    Paragraph(
        "Each question contains two or three statements, four answer options, "
        "and the correct answer immediately below the options in bold.",
        styles["Subtitle"],
    ),
    Paragraph(
        "<b>Source basis:</b> Department of Personnel and Training updated bare "
        "rules. This study material is intended for examination practice; users "
        "should also consult the latest official notifications.",
        styles["Source"],
    ),
    Spacer(1, 18 * mm),
]

current_section = None
letters = "ABCD"
for number, question in enumerate(questions, start=1):
    if question["section"] != current_section:
        current_section = question["section"]
        story.append(Paragraph(current_section, styles["Section"]))

    block = [
        Paragraph(
            f"{number}. Consider the following statements:",
            styles["Question"],
        )
    ]
    for index, statement in enumerate(question["statements"], start=1):
        block.append(
            Paragraph(f"{index}. {statement}", styles["Statement"])
        )
    block.append(
        Paragraph(
            "Which of the statements given above is/are correct?",
            styles["Prompt"],
        )
    )
    for letter, option in zip(letters, question["options"]):
        block.append(
            Paragraph(f"{letter}. {option}", styles["Option"])
        )
    answer_index = letters.index(question["answer"])
    answer_text = question["options"][answer_index]
    block.append(
        Paragraph(
            f"Correct answer: {question['answer']}. {answer_text}",
            styles["Answer"],
        )
    )
    story.append(KeepTogether(block))

doc.build(story)
print(f"Created {OUTPUT}")
