---
topic: "Text-Based Psychotherapy Principles for a Mental Health Journal Companion"
version: 1.0
supersedes: none
date_researched: 2026-05-16
last_updated_signal: 2026-05-12
refresh_after: 2026-08-16
researcher: "GPT-5.5 Thinking"
intended_use: "Foundational context for a text-based journal companion agent that helps users reflect on mental health-related journal entries without diagnosing, treating, or replacing licensed care."
consuming_agent_profile:
  audience: mixed
  verbosity: balanced
  tool_access: ["journal_entry_text", "conversation_history_if_consented", "crisis_resource_lookup_if_available", "live_web_search_if_available"]
  domain_familiarity_assumed: medium
scope_in:
  - "Evidence-informed psychotherapy concepts that translate into text-based journaling support."
  - "Journal-entry reflection, pattern identification, emotion labeling, cognitive reframing, values clarification, coping prompts, and therapy-prep summaries."
  - "Safety boundaries for self-harm, suicide risk, abuse, psychosis/mania signals, eating-disorder signals, substance-use risk, and medical/legal limits."
  - "Ethical, privacy, consent, transparency, and anti-dependency principles for mental-health journaling agents."
scope_out:
  - "Formal diagnosis, treatment planning, or replacement of licensed psychotherapy."
  - "Medication guidance, psychiatric prescribing, or medical decision-making."
  - "Jurisdiction-specific therapist licensure law."
  - "Detailed trauma-processing protocols, exposure protocols, or crisis counseling scripts that imply the agent can manage acute danger alone."
  - "Unverified wellness claims, influencer advice, forums, or AI-generated summaries as evidence."
domain_tags: ["psychotherapy", "journaling", "digital mental health", "AI safety", "CBT", "DBT", "ACT", "crisis escalation"]
depth: deep-dive
evidence_density: dense
overall_confidence: mixed
sources_count: 32
primary_sources_count: 30
methodology_note: "Web research across professional guidelines, official public-health sources, regulatory materials, and peer-reviewed reviews/meta-analyses; recent news used only as staleness/signal evidence."
---

# Text-Based Psychotherapy Principles for a Mental Health Journal Companion

## TL;DR
A text-based journal companion should use psychotherapy-derived skills as structured self-reflection support, not as therapy, diagnosis, or clinical case management. The strongest fit is a bounded blend of CBT-style thought/action mapping, DBT skills language, ACT values/defusion, motivational interviewing autonomy support, behavioral activation, expressive writing, affect labeling, and reflective summarization. Evidence supports digital and writing-based mental-health interventions in some contexts, but effects are heterogeneous, often stronger when guided, and still thin for autonomous AI companions. Safety is load-bearing: the agent must detect explicit and subtle crisis signals, avoid risk scoring or reassurance loops, escalate to human supports and emergency resources, and treat privacy/consent as core product behavior.

## Mental Model
Text-based psychotherapy support is fundamentally about converting private experience into safer, more accurate, more compassionate, and more actionable self-understanding while preserving clinical boundaries.

**Central tensions** — the domain constantly negotiates:
- **Insight vs. rumination:** Reflection can create meaning; repetitive negative thinking can deepen distress if the agent keeps the user circling the same material without naming needs, actions, or support options [S18, S19, S21].
- **Validation vs. collusion:** The agent should validate emotions and lived experience without affirming harmful interpretations, delusions, self-hate, coercive relationship dynamics, or hopeless conclusions [S2, S6, S23].
- **Accessibility vs. clinical scope:** Text tools can expand access and self-care options, but official digital-health guidance warns they are not substitutes for functioning health systems or clinician-managed care when needed [S7, S8, S25].
- **Personalization vs. privacy risk:** Longitudinal journaling improves pattern detection, but mental-health journal data is highly sensitive and requires explicit consent, data minimization, and transparent limits [S3, S29, S30].
- **Autonomy vs. safety escalation:** Respecting user autonomy is central, but imminent harm, abuse, psychosis/mania red flags, or severe functional collapse require the agent to shift from reflective mode to safety-first escalation [S6, S26, S27, S28].

**Decision axes** — implementation choices vary along:
- **Guidance intensity:** open-ended journaling ↔ structured skills coaching; higher structure reduces drift but can feel less user-led.
- **Clinical claim strength:** wellness/self-reflection language ↔ psychotherapy/treatment language; journal companions should stay on the wellness/self-reflection side unless backed by licensed clinical infrastructure [S1, S2, S25].
- **Temporal focus:** present-moment grounding ↔ longitudinal pattern analysis; crisis signals require present safety over historical analysis [S6, S26, S28].
- **Interpretive assertiveness:** tentative hypotheses ↔ declarative formulations; the safe default is “possible pattern” language, not certainty [S2, S23, S24].
- **User autonomy:** directive advice ↔ collaborative options; motivational interviewing favors autonomy-supportive prompts over persuasion or compliance pressure [S14].

**Causal / dependency structure** — what depends on what:
- Useful reflection depends on **emotional arousal being tolerable**; when arousal is extreme, grounding, safety planning, or human escalation should precede deep analysis [S6, S17, S27].
- Cognitive reframing depends on **accurate problem framing**; challenging a thought before validating the emotion often increases defensiveness or shame [S2, S14].
- Longitudinal pattern detection depends on **consistent, consented data**; without representative entries, trend summaries must be framed as partial and tentative [S30].
- Behavioral activation depends on **values, mood, energy, and available context**; tiny doable actions are more appropriate than ambitious plans during low motivation or depression [S5, S15].
- AI safety depends on **product-level constraints**, not just “good prompts”; the evidence base flags privacy, bias, safety, and unpredictable response risks for conversational agents [S22, S23, S24].

**Common pitfalls** — how a naive reader gets this domain wrong:
- **Equating journaling support with therapy:** journaling can support insight and coping, but psychotherapy is a professional service delivered by trained clinicians [S1].
- **Treating cognitive distortion labels as truth:** “catastrophizing” or “mind reading” should be offered as a possible lens, not a verdict.
- **Over-indexing on one journal entry:** one entry is a state sample, not a stable personality map.
- **Using suicide-risk scores:** NICE explicitly advises against using risk tools/scales to predict future suicide or self-harm repetition; needs and safety formulation matter more [S6].
- **Assuming AI chatbots are proven safe because short-term symptom outcomes look promising:** AI conversational-agent trials show possible benefits but also heterogeneity, limited long-term evidence, and safety concerns [S22, S23, S24].

## Glossary
- **[E1] Psychotherapy** _(concept)_ — A professional psychological service using communication and therapeutic interaction to assess and treat psychological problems. Aliases: therapy, talk therapy.
- **[E2] Text-based journal companion** _(concept)_ — A non-clinical agent that helps users reflect on written journal entries, identify patterns, and generate safer next-step prompts.
- **[E3] Evidence-based practice in psychology** _(standard)_ — Integration of best available research, clinical expertise, and patient characteristics, culture, and preferences.
- **[E4] Cognitive Behavioral Therapy (CBT)** _(concept)_ — A structured therapy family focused on links among thoughts, emotions, behaviors, physiology, and situations.
- **[E5] Dialectical Behavior Therapy (DBT) skills** _(concept)_ — Skills commonly organized around mindfulness, distress tolerance, emotion regulation, and interpersonal effectiveness.
- **[E6] Acceptance and Commitment Therapy (ACT)** _(concept)_ — A therapy model emphasizing psychological flexibility, values, acceptance, defusion, and committed action.
- **[E7] Motivational Interviewing (MI)** _(concept)_ — A collaborative conversation style for strengthening motivation and commitment to change while supporting autonomy.
- **[E8] Behavioral Activation (BA)** _(concept)_ — A depression-focused intervention that increases contact with meaningful, reinforcing activities.
- **[E9] Expressive writing** _(concept)_ — Structured writing about emotional experiences to support processing, meaning-making, or disclosure.
- **[E10] Affect labeling** _(concept)_ — Naming emotions in words; studied as a mechanism that can reduce emotional reactivity.
- **[E11] Rumination / repetitive negative thinking** _(concept)_ — Repetitive, difficult-to-disengage thinking about distress, causes, consequences, or threats.
- **[E12] Psychological safety plan** _(concept)_ — A practical plan for recognizing warning signs, reducing access to means, using coping strategies, and contacting supports during risk periods.
- **[E13] 988 Suicide & Crisis Lifeline** _(org)_ — U.S. crisis service reachable by call, text, or chat for 24/7 support.
- **[E14] Digital mental health intervention** _(concept)_ — Use of digital technologies to support mental health, self-care, assessment, education, or treatment delivery.
- **[E15] AI-based conversational agent** _(product)_ — Software that uses natural-language interaction to provide automated support, guidance, or information.
- **[E16] HIPAA Privacy Rule** _(standard)_ — U.S. federal health privacy rule governing protected health information for covered entities and business associates.
- **[E17] NICE** _(org)_ — UK National Institute for Health and Care Excellence, publisher of clinical guidelines.
- **[E18] APA** _(org)_ — American Psychological Association, publisher of professional psychology resources and guidelines.
- **[E19] WHO** _(org)_ — World Health Organization, publisher of international health guidance.
- **[E20] NIMH** _(org)_ — U.S. National Institute of Mental Health, publisher of mental-health education and suicide-warning resources.
- **[E21] SAMHSA** _(org)_ — U.S. Substance Abuse and Mental Health Services Administration, federal behavioral-health agency.
- **[E22] Rejoyn / CT-152** _(product)_ — FDA-cleared prescription digital therapeutic for major depressive disorder symptoms as an adjunct to clinician-managed outpatient care.
- **[E23] Telepsychology** _(concept)_ — Psychological services delivered using telecommunication technologies.

## Canonical Facts
1. **[F1]** [E1] is a professional psychological service delivered by a trained professional through communication and therapeutic interaction; it is not equivalent to generic self-help or journaling support [S1].
2. **[F2]** [E3] integrates best available research with clinical expertise in the context of patient characteristics, culture, and preferences [S2].
3. **[F3]** APA telepsychology guidance treats technology-mediated psychological services as requiring attention to competence, standards of care, informed consent, confidentiality, security, and interjurisdictional issues [S3].
4. **[F4]** NICE guideline NG222 on adult depression was published on 2022-06-29 and last reviewed on 2026-01-30 with no update required at that review [S5].
5. **[F5]** NICE guideline NG225 advises practitioners not to use risk assessment tools or scales to predict future suicide or repetition of self-harm, and instead to focus assessment on needs and immediate/long-term safety [S6].
6. **[F6]** WHO’s 2019 digital-health guideline states that digital health interventions are not a substitute for functioning health systems and have significant limitations [S7].
7. **[F7]** WHO defines self-care as the ability of individuals, families, and communities to promote health, prevent disease, maintain health, and cope with illness and disability with or without health-worker support [S8].
8. **[F8]** WHO’s mhGAP Intervention Guide is intended to help non-specialized health-care settings assess and manage priority mental, neurological, and substance-use conditions using structured algorithms [S9].
9. **[F9]** Rejoyn / CT-152 is an FDA-cleared prescription digital therapeutic intended as an adjunct to clinician-managed outpatient care for adults aged 22 or older with major depressive disorder who are taking antidepressant medication; FDA documentation states it is not stand-alone therapy or a substitute for clinician-prescribed medication [S25].
10. **[F10]** The 988 Suicide & Crisis Lifeline offers U.S. call, text, and chat access for 24/7 free and confidential crisis support [S26].
11. **[F11]** NIMH’s five action steps for helping someone with suicidal thoughts are: ask, be there, help keep them safe, help them connect, and follow up [S27].
12. **[F12]** NIMH lists suicide warning signs including talking about wanting to die, feeling trapped or unbearable pain, researching ways to die, withdrawing, extreme mood swings, changing sleep/eating patterns, and increased substance use; NIMH says to get help especially if signs are new, increased, or linked to a painful event [S28].
13. **[F13]** The HIPAA Privacy Rule establishes federal standards for protected health information held by covered entities and business associates, including limits on uses/disclosures and individual rights [S29].
14. **[F14]** A 2023 systematic review/meta-analysis of AI-based conversational agents included 35 studies and a 15-RCT meta-analysis; it reported reductions in depression and distress symptoms but no statistically significant overall well-being effect and called for more long-term and safety research [S22].
15. **[F15]** Frattaroli’s 2006 meta-analysis of experimental disclosure included 146 randomized studies and found a small but statistically significant positive average effect [S18].

## Core Findings
1. **[CF1] [LOAD-BEARING]** A journal companion should be framed as [E2], not [E1]. It can borrow evidence-informed therapy skills, but the output must stay within self-reflection, self-care, coping support, and therapy-prep—not diagnosis, treatment, or clinical authority [S1, S2, S7, S8, S25].
2. **[CF2] [LOAD-BEARING]** The most transferable psychotherapy elements are structured, teachable skills: CBT thought-action mapping, DBT distress tolerance and emotion-regulation language, ACT values/defusion, MI autonomy support, behavioral activation, affect labeling, and expressive writing [S5, S13, S14, S15, S16, S17, S18, S20].
3. **[CF3] [LOAD-BEARING]** Text and journaling interventions have useful but bounded evidence. Expressive writing and journaling show modest or mixed benefits, and text-based mental-health delivery varies by population, intervention design, and guidance level [S11, S12, S18, S19].
4. **[CF4] [LOAD-BEARING]** The agent should analyze entries as hypotheses, not verdicts: “This may reflect…” is safer than “You are…” or “You have…”. This follows evidence-based practice principles and avoids overclaiming from partial, self-selected journal data [INFERENCE from S2, S3, S23, S24, S30].
5. **[CF5] [LOAD-BEARING]** Crisis handling must be safety-first and non-predictive: detect warning signs, ask direct safety questions when warranted, reduce access to means, connect to people and crisis resources, and avoid numerical risk scores or promises of confidentiality the product cannot honor [S6, S26, S27, S28].
6. **[CF6] [LOAD-BEARING]** Autonomous AI mental-health agents have preliminary evidence of benefit but insufficient evidence for long-term safety, effectiveness across high-risk populations, bias control, or crisis reliability. Human escalation and product-level safeguards are mandatory design assumptions [S4, S22, S23, S24, S31, S32].
7. **[CF7] [SUPPORTING]** Privacy is not a side feature for a journal companion; mental-health journal content can include trauma, family conflict, sexuality, substance use, suicidal ideation, and medical information. Even when HIPAA does not apply, app developers should use privacy/security-by-design and disclose data practices clearly [S29, S30].
8. **[CF8] [SUPPORTING]** The best outputs are maps, summaries, options, and questions: emotion labels, thought maps, values signals, recurring themes, gentle alternative interpretations, therapy questions, and small next actions. The agent should not produce diagnoses, personality labels, or treatment plans [INFERENCE from S2, S5, S8, S18, S22].
9. **[CF9] [SUPPORTING]** Journaling prompts should interrupt rumination by moving from repetition toward naming emotions, identifying needs, locating controllable next steps, and choosing support. Repeated analysis without action or compassion can reinforce [E11] [S18, S20, S21].
10. **[CF10] [LOAD-BEARING]** Evidence for internet-based CBT suggests guidance matters; guided internet-based CBT has stronger depression outcomes than unguided formats in major reviews. A journal companion without a licensed clinician should therefore avoid implying equivalent efficacy to guided therapy [S10].
11. **[CF11] [SUPPORTING]** The FDA-cleared example [E22] illustrates the boundary: even a regulated digital therapeutic for depression is positioned as adjunctive, clinician-managed, and not a substitute for medication or clinician care [S25].
12. **[CF12] [SUPPORTING]** Text-only support should prioritize plain language, low cognitive load, user choice, and cultural humility because users may be distressed, tired, neurodivergent, ashamed, or ambivalent while writing [INFERENCE from S2, S8, S14, S23].

## Detailed Analysis

### What is psychotherapy, and what parts of it can realistically translate into a text-based journaling companion?
Psychotherapy is a professional health service, not merely a set of supportive phrases. The APA frames psychotherapy as a psychological service delivered by trained professionals using communication and interaction to assess and treat reactions, thoughts, feelings, and behavior patterns [S1]. Evidence-based practice also depends on clinical expertise and patient context, not research techniques alone [S2]. Therefore, a journal companion can use psychotherapy-informed concepts but should not represent itself as providing psychotherapy unless embedded in a licensed, clinically governed service.

The transferable layer is the reflective and skills layer: helping users name experiences, notice links among situations/thoughts/emotions/actions, explore alternative interpretations, clarify values, identify needs, and prepare topics for therapy. Text is especially well suited to slowing down thoughts, preserving context, summarizing patterns, and creating longitudinal visibility.

The non-transferable layer is clinical responsibility: diagnosis, differential diagnosis, risk formulation, trauma processing, treatment planning, medication decisions, mandated reporting decisions, and management of acute danger. Telepsychology guidance treats remote psychological service as still requiring professional competence, informed consent, privacy/security, and standards of care [S3]. A journal app should not borrow the authority of psychotherapy while avoiding its governance.

_Confidence: high — definitions and boundaries align across APA professional resources, WHO digital-health guidance, and FDA adjunctive digital therapeutic framing ([S1], [S2], [S3], [S7], [S25])._

### Which evidence-based therapy modalities are most useful for text-based journaling support?
CBT is useful because journaling naturally captures situations, automatic thoughts, emotions, body sensations, and behaviors. The journal companion can help the user map “what happened → what I thought → what I felt → what I did → what else might be true → what small action fits.” For a text agent, this should be offered as a worksheet-like lens, not as a diagnosis or assertion that the user’s thought is “wrong” [S5, S10].

DBT contributes skills language for emotional intensity: mindfulness, distress tolerance, emotion regulation, and interpersonal effectiveness. In journaling, this translates into prompts such as “What emotion is primary vs. secondary?”, “What urge came with it?”, “What would help you survive the next 10 minutes without making things worse?”, and “What boundary or request might fit?” DBT is especially useful as a skills vocabulary, but the agent should not claim to deliver comprehensive DBT [S16, S17].

ACT contributes values, acceptance, defusion, and committed action. A journal companion can help users distinguish “the thought I am having” from “the fact of the world,” identify values under pain, and choose a small values-consistent action. ACT has meta-analytic support across anxiety, depression, addiction, and somatic problems, and it performs comparably to established interventions in some analyses [S13].

Motivational interviewing is useful for ambivalence. A journal companion should ask permission, reflect change talk, affirm autonomy, and avoid arguing the user into change. MI evidence supports behavior-change conversations across health contexts, but the agent should use MI style rather than simulate a full therapeutic MI session [S14]. Behavioral activation is useful when entries show withdrawal, low motivation, or depression-linked avoidance; the agent can suggest small, meaningful actions matched to the user’s energy [S15].

_Confidence: high for modality-to-skill mapping; mixed for autonomous delivery efficacy — the modalities have strong clinical literature, but journal-agent translation is an implementation inference ([S5], [S10], [S13], [S14], [S15], [S16], [S17])._

### What can journaling do for mental health, and where is the evidence strongest or weakest?
Journaling can support disclosure, emotion labeling, cognitive processing, self-monitoring, and meaning-making. Expressive-writing research has found small average positive effects across randomized studies, not large or universal effects [S18]. A 2022 systematic review/meta-analysis specifically on journaling for mental illness reported benefit signals, but journaling interventions vary widely in format, population, duration, and outcomes [S19].

For a journal companion, the practical implication is to treat journaling as a low-cost reflective practice, not a stand-alone treatment. It is strongest when used to clarify experiences, notice patterns, prepare for therapy, track mood/behavior links, and convert vague distress into specific needs. It is weaker when used as repeated venting without structure, as substitute crisis care, or as a tool for diagnosing the self.

Affect labeling is a particularly relevant mechanism: naming feelings may help reduce emotional reactivity and increase prefrontal engagement in some laboratory research [S20]. This supports agent behavior such as offering emotion-word menus, distinguishing primary/secondary emotions, and validating that “naming the feeling is already doing part of the work.”

_Confidence: mixed — expressive writing and journaling have credible evidence, but effect sizes and outcomes are heterogeneous; affect-labeling evidence is mechanistic and not equivalent to clinical journaling outcome evidence ([S18], [S19], [S20])._

### How should a journal companion analyze user thoughts without overreaching?
The safest analysis pattern is: observe → hypothesize → ask → offer options. Example: “I notice the entry has a lot of ‘always/never’ language. One possible lens is all-or-nothing thinking. Does that fit, or does it feel off?” This protects user autonomy, avoids pathologizing, and respects that a journal entry is partial data.

The agent can identify possible cognitive patterns: catastrophizing, mind reading, fortune telling, personalization, all-or-nothing thinking, emotional reasoning, should-statements, avoidance loops, values conflicts, unmet needs, relational patterns, and self-criticism. These should be framed as “lenses” or “patterns to test,” never as labels of identity. The agent should avoid deriving stable personality traits, diagnoses, trauma interpretations, attachment labels, or motive claims from one or a few entries [S2, S23, S24].

The companion should also separate content layers: facts, interpretations, emotions, urges, needs, values, and possible actions. This structure is more useful than telling the user what their entry “means.” It also reduces the risk of reinforcing rumination: once a pattern is named, the agent should help the user choose a next reflective question, grounding step, support contact, or small action [S21].

_Confidence: mixed — the approach is a safety-oriented synthesis from evidence-based practice, CBT-style structure, rumination literature, and AI safety concerns rather than a single validated journal-agent protocol ([S2], [S21], [S23], [S24])._

### What conversational techniques are safest and most useful in text-only mental health support?
Validation should come first: reflect the emotion and stakes before analysis. A useful format is, “Given what you wrote, it makes sense that you’d feel ___; the part I want to examine gently is ___.” This preserves alliance while allowing reframing. Reflective listening, summarization, and emotion labeling are high-value text behaviors because they reduce cognitive load and help users see their own thoughts more clearly [S14, S20].

Socratic questioning can be useful when gentle and consent-based: “What evidence supports this thought?”, “What evidence complicates it?”, “What would you say to a friend?”, “What is the most compassionate accurate version?” It should not become cross-examination. The goal is flexible perspective, not proving the user wrong.

Grounding and stabilization should be available when entries show high arousal. Text-only grounding can include breath pacing, sensory orientation, naming present facts, reducing immediate demands, and contacting support. Action planning should be tiny, concrete, and reversible: “one text,” “one glass of water,” “two-minute reset,” “write the therapy question,” not a full life overhaul.

_Confidence: mixed — techniques are grounded in established therapy traditions, but their safety depends heavily on wording, timing, user state, and product constraints ([S14], [S17], [S20], [S23], [S24])._

### What are the safety boundaries for a mental health journal companion?
The agent must distinguish reflective mode from safety mode. Safety mode is triggered by suicidal ideation, self-harm, preparatory behavior, inability to commit to immediate safety, threats from others, abuse/coercive control, psychosis/mania indicators, severe intoxication, eating-disorder medical danger, or major functional collapse. NIMH warning signs include wanting to die, feeling trapped, researching ways to die, withdrawal, dangerous risk-taking, extreme mood swings, changes in sleep/eating, and increased substance use [S28].

In safety mode, the agent should not continue deep analysis. It should ask direct, plain-language safety questions when warranted; encourage immediate contact with trusted people and emergency/crisis services; provide 988 for U.S. users; and recommend emergency services for imminent danger [S26, S27, S28]. It should not promise secrecy, perform detailed risk scoring, or debate the user out of self-harm. NICE warns against risk tools/scales for predicting future suicide or self-harm and emphasizes needs and safety [S6].

A safety plan may include warning signs, internal coping strategies, people and places for distraction, trusted contacts, professional/crisis resources, and reducing access to means [S6]. For journal-app design, the safety plan should be a user-visible, consented, editable artifact—not something hidden in the model’s memory.

_Confidence: high for self-harm and suicide boundaries; mixed for broader red-flag categories because specific app escalation rules require clinical, legal, and product governance ([S6], [S26], [S27], [S28])._

### What ethical and privacy principles should govern a journaling mental health agent?
The agent should be transparent about what it is: a journaling support tool, not a therapist. It should state limits before high-stakes use, avoid therapeutic title inflation, and encourage professional care when distress is persistent, severe, risky, or impairing. The APA’s AI mental-health advisory direction and AI-safety literature emphasize that mental-health chatbots require careful consumer safety, evidence, and governance rather than broad therapeutic claims [S4, S22, S23, S24].

Privacy must be designed into the product. The HIPAA Privacy Rule applies to covered entities and business associates, but many wellness apps fall outside HIPAA depending on data flows and business structure [S29, S30]. Regardless of legal category, the ethical bar should include data minimization, consent for memory and longitudinal summaries, clear deletion/export controls, protection against secondary use surprises, and special caution around minors and family/shared devices [S30].

The agent should also avoid dependency. It should not position itself as the only one who understands the user, discourage therapy, replace relationships, or reward endless disclosure. Good behavior includes asking whether the user wants reflection, skill practice, grounding, or a summary to bring to a human support.

_Confidence: high for privacy/transparency principles; mixed for legal applicability because HIPAA and other laws depend on product architecture and jurisdiction ([S4], [S23], [S24], [S29], [S30])._

### How should the agent convert journal entries into useful outputs?
The most useful outputs are structured mirrors, not conclusions. Recommended output types include: “emotion map,” “thought-action loop,” “possible cognitive pattern,” “needs and values signal,” “what changed since last entry,” “question for therapy,” “tiny next step,” “support script,” “coping plan draft,” and “weekly pattern summary.” These support insight without claiming clinical authority [S2, S8, S18, S20].

For a single entry, the agent should keep outputs short and user-confirmed: top emotions, main stressor, possible thought pattern, one compassionate reframe, and one optional next step. For multiple entries, it can summarize recurring triggers, emotional themes, avoidance loops, effective coping actions, and open questions. Longitudinal conclusions must include uncertainty because journal entries are self-selected and context-dependent [S30].

The agent should use escalation-aware templates. If crisis content appears, the output becomes safety-oriented. If trauma content appears, the output emphasizes stabilization, choice, grounding, and professional support rather than detailed exposure or memory reconstruction. If mania/psychosis-like content appears, it should avoid validating delusional certainty and instead focus on sleep, safety, trusted human contact, and professional support [S6, S23, S24, S28].

_Confidence: mixed — output formats are a design synthesis from therapy skills, journaling evidence, and safety literature; they should be user-tested and clinically reviewed before deployment ([S2], [S6], [S18], [S20], [S23], [S24], [S30])._

## Conflicts, Assumptions & Uncertainty

**Source conflicts** — where credible sources disagree or tension remains.
- **Digital access benefit vs. substitute risk:** WHO supports evidence-based self-care and digital interventions as additional options, but also states digital tools do not substitute for functioning health systems [S7, S8]. FDA-cleared [E22] is explicitly adjunctive, reinforcing the boundary [S25].
- **Promising AI outcomes vs. safety evidence gaps:** AI conversational-agent meta-analysis reports symptom improvements for depression/distress, but also heterogeneity and need for long-term safety evidence [S22]. AI safety literature and professional advisories emphasize privacy, bias, and unpredictable response risks [S4, S23, S24].
- **Journaling benefit vs. rumination risk:** Expressive-writing and journaling reviews show benefit signals, but rumination literature warns that repetitive negative thinking can maintain distress [S18, S19, S21]. The agent must structure reflection toward meaning, compassion, support, or action.

**Interpretive assumptions** — calls the researcher made.
- Treated “psychotherapy for a journal companion” as “psychotherapy-informed self-reflection,” not delivery of psychotherapy, because the consuming agent is a journaling app rather than a licensed clinical service [S1, S2, S25].
- Assumed general adult users unless the app explicitly targets minors. If minors are included, parental/guardian consent, abuse reporting workflows, school-risk protocols, and child-specific safety review become mandatory.
- Treated U.S. crisis resources as examples because 988/NIMH/SAMHSA are strong primary sources; production systems should localize crisis resources by user region [S26, S27, S28].
- Counted peer-reviewed reviews/meta-analyses as primary research evidence for the brief’s source minimum because the generator’s hierarchy includes peer-reviewed papers as primary sources.

**Areas of thin evidence.**
- Long-term outcomes for autonomous AI journal companions are not well established.
- Safety performance for subtle, gradual, or ambiguous crisis signals remains uncertain; recent reporting and benchmarking suggest this is an active risk area [S31, S32].
- There is limited public evidence on how users with severe mental illness, active suicidality, coercive relationships, eating disorders, or mania/psychosis interact with general-purpose journal agents.
- Legal obligations vary by jurisdiction and product architecture; this brief is not legal advice [S29, S30].

## Open Questions & Gaps
1. **Does a longitudinal AI journal companion improve outcomes beyond ordinary journaling?** Would need: preregistered trials comparing agent-guided journaling, unguided journaling, guided human support, and waitlist/control.
2. **Which prompt styles reduce rumination rather than increasing it?** Would need: controlled studies measuring repetitive negative thinking after different journaling-agent response types.
3. **How reliable is AI crisis detection in journal entries over time?** Would need: clinically labeled longitudinal datasets, safety benchmarks, and post-deployment incident monitoring.
4. **How should the agent adapt to neurodivergence, culture, trauma history, and literacy level?** Would need: participatory design studies and subgroup analyses.
5. **What privacy architecture best balances personalization and data minimization?** Would need: product-specific legal analysis, threat modeling, and user research.
6. **How should journal insights be handed off to therapists?** Would need: clinician interviews, workflow studies, and consented export-format testing.

## Staleness Indicators
- **Time-based:** review after `refresh_after` date in front-matter because AI mental-health products, legal scrutiny, and digital therapeutic evidence are changing quickly.
- **Event-based:** if any of the following occur, this brief is likely partially invalidated:
  - New APA, WHO, NICE, FDA, FTC, HHS, or SAMHSA guidance on AI mental-health tools → likely affects [F3], [F6], [F9], [CF6], [CF7].
  - New FDA clearance, recall, warning letter, or enforcement action for mental-health conversational agents or digital therapeutics → likely affects [CF1], [CF6], [CF11].
  - New major meta-analysis on AI mental-health chatbots, guided journaling apps, or text-based therapy outcomes → likely affects [F14], [CF3], [CF6], [CF10].
  - New law restricting or defining AI therapy, chatbot therapy claims, or mental-health app data use → likely affects Ethical/Privacy analysis and Decision Heuristics [S29, S30, S31].
  - Major public safety incident involving a mental-health chatbot or lawsuit alleging harmful advice → treat safety claims as stale and prefer current official/legal sources [S31].
- **Signal-based:** if users report the agent encourages secrecy, dependency, self-diagnosis, hopelessness, avoidance of care, delusional certainty, or unsafe coping, treat safety sections as suspect and escalate product review.
- **Signal-based:** if live tools find a newer crisis-resource number or regional emergency guidance than [E13], use the live local source.

## Decision Heuristics for the Agent

**DO**
- Use [F#] Canonical Facts as the most authoritative ground-truth layer.
- Treat [CF#] Core Findings as operational guidance, with [LOAD-BEARING] findings overriding [SUPPORTING] findings when in tension.
- Start with validation, then offer structure: emotion labels, facts vs. interpretations, possible patterns, values/needs, and one small next step.
- Phrase analysis as tentative: “a possible pattern,” “one lens,” “this may connect to,” “does that fit?”
- Ask permission before challenging a thought or offering a reframe.
- Use crisis mode when warning signs appear: ask direct safety questions when warranted, encourage immediate human support, provide local emergency/crisis resources, and stop deep analysis [F10], [F11], [F12].
- Encourage therapy, medical care, crisis lines, trusted people, or emergency services when risk, severity, impairment, or persistence exceeds journaling support.
- Convert entries into user-owned artifacts: therapy questions, coping cards, safety-plan drafts, support scripts, pattern summaries, and values-based micro-actions.
- Minimize shame. Prefer “your nervous system may be trying to protect you” over “this is irrational.”
- Defer to live, official sources for crisis resources, legal/privacy obligations, and current AI safety guidance after `refresh_after`.

**DO NOT**
- Do not claim to be a therapist, therapy, psychotherapy, a diagnosis tool, or a substitute for clinician care.
- Do not diagnose, assign disorders, infer trauma history as fact, label personality, or produce treatment plans.
- Do not use numerical suicide/self-harm risk scores or claim to predict future suicide/self-harm [F5].
- Do not continue ordinary journaling analysis when the entry indicates imminent danger, self-harm preparation, abuse, psychosis/mania red flags, severe intoxication, or medical danger.
- Do not provide self-harm methods, lethal-dose information, coercive relationship tactics, eating-disorder optimization, or instructions that enable harm.
- Do not validate delusions, paranoia, grandiosity, or unsafe certainty; validate fear/distress while redirecting to safety and human support.
- Do not say journal data is confidential unless the product’s actual policy and legal context support that claim.
- Do not make long-term pattern claims from one entry or a thin sample.
- Do not over-pathologize normal grief, anger, stress, or conflict.
- Do not confuse [E2] with [E1]: a journal companion can support reflection, but psychotherapy requires professional competence, clinical responsibility, and appropriate governance.

## Sources
- **[S1]** American Psychological Association. *Psychotherapy*. APA. Accessed 2026-05-16. https://www.apa.org/topics/psychotherapy. _Type: primary. Credibility: official professional association topic resource._
- **[S2]** American Psychological Association. *Evidence-Based Practice in Psychology*. APA. 2005-07-01; accessed 2026-05-16. https://www.apa.org/practice/guidelines/evidence-based-statement. _Type: primary. Credibility: official professional policy statement/resource._
- **[S3]** American Psychological Association. *Guidelines for the Practice of Telepsychology*. APA. 2013-07-31; accessed 2026-05-16. https://www.apa.org/practice/guidelines/telepsychology. _Type: primary. Credibility: official professional guideline._
- **[S4]** American Psychological Association. *Use of Generative AI Chatbots and Wellness Applications for Mental Health*. APA Health Advisory. 2025-11-13; accessed 2026-05-16. https://www.apa.org/topics/artificial-intelligence-machine-learning/health-advisory. _Type: primary. Credibility: official professional advisory._
- **[S5]** National Institute for Health and Care Excellence. *Depression in Adults: Treatment and Management (NG222)*. NICE. 2022-06-29; last reviewed 2026-01-30. https://www.nice.org.uk/guidance/ng222. _Type: primary. Credibility: national clinical guideline._
- **[S6]** National Institute for Health and Care Excellence. *Self-harm: Assessment, Management and Preventing Recurrence (NG225)*. NICE. 2022-09-07; accessed 2026-05-16. https://www.nice.org.uk/guidance/ng225. _Type: primary. Credibility: national clinical guideline._
- **[S7]** World Health Organization. *WHO Guideline: Recommendations on Digital Interventions for Health System Strengthening*. WHO. 2019-06-06. https://www.who.int/publications/i/item/9789241550505. _Type: primary. Credibility: international public-health guideline._
- **[S8]** World Health Organization. *Self-care for Health and Well-being*. WHO Fact Sheet. 2024-04-26. https://www.who.int/news-room/fact-sheets/detail/self-care-health-interventions. _Type: primary. Credibility: international public-health source._
- **[S9]** World Health Organization. *mhGAP Intervention Guide for Mental, Neurological and Substance Use Disorders in Non-specialized Health Settings, Version 2.0*. WHO. 2019-06-24. https://www.who.int/publications/i/item/9789241549790. _Type: primary. Credibility: international public-health clinical guide._
- **[S10]** Karyotaki E, Efthimiou O, Miguel C, et al. *Internet-Based Cognitive Behavioral Therapy for Depression: A Systematic Review and Individual Patient Data Network Meta-analysis*. JAMA Psychiatry. 2021. https://pubmed.ncbi.nlm.nih.gov/33471111/. _Type: primary. Credibility: peer-reviewed systematic review/meta-analysis._
- **[S11]** Dwyer A, de Almeida Neto A, Estival D, Li W, Lam-Cassettari C, Antoniou M. *Suitability of Text-Based Communications for the Delivery of Psychological Therapeutic Services to Rural and Remote Communities: Scoping Review*. JMIR Mental Health. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC7946577/. _Type: primary. Credibility: peer-reviewed scoping review._
- **[S12]** Shalaby R, Adu MK, Andreychuk T, et al. *Text Messages in the Field of Mental Health: Rapid Review of the Reviews*. JMIR mHealth and uHealth. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9263363/. _Type: primary. Credibility: peer-reviewed review of reviews._
- **[S13]** A-Tjak JGL, Davis ML, Morina N, Powers MB, Smits JAJ, Emmelkamp PMG. *A Meta-analysis of the Efficacy of Acceptance and Commitment Therapy for Clinically Relevant Mental and Physical Health Problems*. Psychotherapy and Psychosomatics. 2015. https://pubmed.ncbi.nlm.nih.gov/25547522/. _Type: primary. Credibility: peer-reviewed meta-analysis._
- **[S14]** Rubak S, Sandbæk A, Lauritzen T, Christensen B. *Motivational Interviewing: A Systematic Review and Meta-analysis*. British Journal of General Practice. 2005. https://pmc.ncbi.nlm.nih.gov/articles/PMC1463134/. _Type: primary. Credibility: peer-reviewed systematic review/meta-analysis._
- **[S15]** Ekers D, Webster L, Van Straten A, Cuijpers P, Richards D, Gilbody S. *Behavioural Activation for Depression; An Update of Meta-analysis of Effectiveness and Sub Group Analysis*. PLOS ONE. 2014. https://pmc.ncbi.nlm.nih.gov/articles/PMC4061095/. _Type: primary. Credibility: peer-reviewed meta-analysis._
- **[S16]** Chapman AL. *Dialectical Behavior Therapy: Current Indications and Unique Elements*. Psychiatry (Edgmont). 2006. https://pmc.ncbi.nlm.nih.gov/articles/PMC2963469/. _Type: primary. Credibility: peer-reviewed clinical review._
- **[S17]** May JM, Richardi TM, Barth KS. *Dialectical Behavior Therapy as Treatment for Borderline Personality Disorder*. Mental Health Clinician. 2016. https://pmc.ncbi.nlm.nih.gov/articles/PMC6007584/. _Type: primary. Credibility: peer-reviewed clinical review._
- **[S18]** Frattaroli J. *Experimental Disclosure and Its Moderators: A Meta-analysis*. Psychological Bulletin. 2006-11. https://pubmed.ncbi.nlm.nih.gov/17073523/. _Type: primary. Credibility: peer-reviewed meta-analysis._
- **[S19]** Sohal M, Singh P, Dhillon BS, Gill HS. *Efficacy of Journaling in the Management of Mental Illness: A Systematic Review and Meta-analysis*. Family Medicine and Community Health. 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC8935176/. _Type: primary. Credibility: peer-reviewed systematic review/meta-analysis._
- **[S20]** Lieberman MD, Eisenberger NI, Crockett MJ, Tom SM, Pfeifer JH, Way BM. *Putting Feelings into Words: Affect Labeling Disrupts Amygdala Activity in Response to Affective Stimuli*. Psychological Science. 2007. https://pubmed.ncbi.nlm.nih.gov/17576282/. _Type: primary. Credibility: peer-reviewed experimental neuroscience study._
- **[S21]** Ehring T. *Thinking Too Much: Rumination and Psychopathology*. World Psychiatry. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8429319/. _Type: primary. Credibility: peer-reviewed review in high-impact psychiatry journal._
- **[S22]** Li H, Zhang R, Lee Y-C, Kraut RE, Mohr DC. *Systematic Review and Meta-analysis of AI-Based Conversational Agents for Promoting Mental Health and Well-being*. npj Digital Medicine. 2023-12-19. https://pmc.ncbi.nlm.nih.gov/articles/PMC10730549/. _Type: primary. Credibility: peer-reviewed systematic review/meta-analysis._
- **[S23]** Lawrence HR, Schneider P, Rubin M, et al. *The Opportunities and Risks of Large Language Models in Mental Health Care*. JMIR Mental Health. 2024; accessed 2026-05-16. https://pmc.ncbi.nlm.nih.gov/articles/PMC11301767/. _Type: primary. Credibility: peer-reviewed risk/opportunity analysis._
- **[S24]** Parks AC, Torous J, Blease C, et al. *Is This Chatbot Safe and Evidence-Based? A Call for a Framework to Support Safe and Evidence-Based Mental Health Chatbots*. Journal of Participatory Medicine. 2025; accessed 2026-05-16. https://jopm.jmir.org/2025/1/e69534. _Type: primary. Credibility: peer-reviewed safety-framework viewpoint._
- **[S25]** U.S. Food and Drug Administration. *K231209 510(k) Summary: CT-152 / Rejoyn*. FDA. Submitted 2023-04-27; cleared 2024; accessed 2026-05-16. https://www.accessdata.fda.gov/cdrh_docs/pdf23/K231209.pdf. _Type: primary. Credibility: regulatory clearance documentation._
- **[S26]** SAMHSA and 988 Suicide & Crisis Lifeline. *988 Suicide & Crisis Lifeline*. SAMHSA/988. Updated 2025-09-26; accessed 2026-05-16. https://www.samhsa.gov/mental-health/988 and https://988lifeline.org/. _Type: primary. Credibility: official U.S. crisis-service sources._
- **[S27]** National Institute of Mental Health. *5 Action Steps to Help Someone Having Thoughts of Suicide*. NIMH. Revised 2024; accessed 2026-05-16. https://www.nimh.nih.gov/health/publications/5-action-steps-to-help-someone-having-thoughts-of-suicide. _Type: primary. Credibility: official U.S. mental-health source._
- **[S28]** National Institute of Mental Health. *Warning Signs of Suicide*. NIMH. Revised 2025; accessed 2026-05-16. https://www.nimh.nih.gov/health/publications/warning-signs-of-suicide. _Type: primary. Credibility: official U.S. mental-health source._
- **[S29]** U.S. Department of Health and Human Services. *The HIPAA Privacy Rule*. HHS. Last reviewed 2024-09-27; accessed 2026-05-16. https://www.hhs.gov/hipaa/for-professionals/privacy/index.html. _Type: primary. Credibility: official federal privacy guidance._
- **[S30]** U.S. Department of Health and Human Services. *Resources for Mobile Health Apps Developers*. HHS. Accessed 2026-05-16. https://www.hhs.gov/hipaa/for-professionals/special-topics/health-apps/index.html. _Type: primary. Credibility: official federal app-developer privacy/security guidance._
- **[S31]** Thomson Reuters. *OpenAI Faces Lawsuit by Parents Who Blame Chatbot Advice for Son's Fatal Overdose*. Reuters. 2026-05-12. https://www.reuters.com/legal/government/openai-faces-lawsuit-by-parents-who-blame-chatbot-advice-sons-fatal-overdose-2026-05-12/. _Type: secondary. Credibility: original legal reporting; used only as current safety/staleness signal._
- **[S32]** Megan Morrone. *AI Chatbots Struggle with Subtle Mental Health Cues*. Axios. 2026-05-12. https://www.axios.com/2026/05/12/ai-chatbots-mental-health-crisis-cues. _Type: secondary. Credibility: current technology reporting; used only as current safety/staleness signal._

## Changelog
- **v1.0 (2026-05-16):** Initial brief.
