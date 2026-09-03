"""Renderer separati per il report decisionale e per l'allegato tecnico.

Il report principale traduce esclusivamente dati già prodotti dal motore in
prosa breve. L'allegato conserva invece valori raw, policy, provenienza e trace.
Nessuna funzione di questo modulo ricalcola applicabilità, esiti o priorità.
"""

from __future__ import annotations

import json
from collections.abc import Iterable, Mapping, Sequence
from typing import Any

ITALIAN_VALUES = {
    "important": "importante",
    "essential": "essenziale",
    "compliant": "soddisfatto",
    "non_compliant": "non soddisfatto",
    "not_verifiable": "non verificabile",
    "not_applicable": "non applicabile",
    "partially_compliant": "parzialmente soddisfatto",
    "high": "alta",
    "medium": "media",
    "low": "bassa",
    "insufficient": "insufficiente",
    "complete": "completa",
    "partial": "parziale",
}

AREA_LABELS = {
    "access_control": "il controllo degli accessi",
    "asset_management": "la gestione degli asset",
    "backup_recovery": "il backup e il ripristino",
    "cryptography": "la crittografia",
    "data_protection": "la protezione dei dati",
    "endpoint_security": "la sicurezza degli endpoint",
    "identity_access": "le identità e gli accessi",
    "logging_monitoring": "il logging e il monitoraggio",
    "monitoring_detection": "il monitoraggio e il rilevamento",
    "network_security": "la sicurezza di rete",
    "patch_management": "la gestione degli aggiornamenti",
    "physical_security": "la sicurezza fisica",
    "security_monitoring": "il monitoraggio di sicurezza",
    "supply_chain_technical": "la sicurezza tecnica dei fornitori",
    "system_lifecycle": "il ciclo di vita dei sistemi",
    "vulnerability_management": "la gestione delle vulnerabilità",
}


SOURCE_LABELS = {
    "backup-manager": "dal gestore dei backup",
    "CMDB": "dalla CMDB",
    "configuration-manager": "dal gestore delle configurazioni",
    "endpoint-platform": "dalla piattaforma di protezione degli endpoint",
    "facilities": "dalla funzione Facilities",
    "IAM": "dal sistema IAM",
    "logging-platform": "dalla piattaforma di logging",
    "monitoring-platform": "dalla piattaforma di monitoraggio",
    "network-manager": "dal gestore della rete",
    "patch-manager": "dal gestore degli aggiornamenti",
    "service-catalog": "dal catalogo aziendale",
    "crisis-platform": "dalla piattaforma di gestione delle emergenze",
    "vulnerability-manager": "dal gestore delle vulnerabilità",
    "vulnerability-scanner": "dallo scanner delle vulnerabilità",
}


ACTION_LABELS = {
    "Censire componenti versioni e stato di autorizzazione": "Censire i componenti, le versioni e lo stato di autorizzazione",
    "Documentare origine destinazione protocolli e autorizzazione dei flussi": "Documentare l'origine, la destinazione, i protocolli e l'autorizzazione dei flussi",
    "Monitorare fonti ACN CERT e ISAC pertinenti alle tecnologie utilizzate": "Monitorare le fonti ACN CERT e ISAC pertinenti alle tecnologie utilizzate",
    "Documentare l'approfondimento applicato al vulnerability assessment": "Documentare l'approfondimento applicato alla valutazione delle vulnerabilità",
    "Acquisire evidenza corrente delle protezioni fisiche applicabili": "Acquisire un'evidenza corrente delle protezioni fisiche applicabili",
    "Cifrare i supporti rimovibili secondo classificazione e baseline approvata": "Cifrare i supporti rimovibili secondo la classificazione e la baseline approvata",
    "Adeguare frequenza e copie offline al piano approvato": "Adeguare la frequenza e le copie offline al piano approvato",
    "Registrare manutenzione e procedure di dismissione sicura": "Registrare le attività di manutenzione e le procedure di dismissione sicura",
    "Registrare accessi amministrativi e remoti e proteggere i log per il periodo pianificato": "Registrare gli accessi amministrativi e remoti e proteggere i log per il periodo pianificato",
    "Predisporre testare e mantenere comunicazioni di emergenza protette": "Predisporre, testare e mantenere comunicazioni di emergenza protette",
    "Calibrare e riesaminare soglie e regole di anomalia": "Calibrare e riesaminare le soglie e le regole di anomalia",
    "Installare configurare mantenere e monitorare la protezione endpoint appropriata": "Installare, configurare, mantenere e monitorare la protezione degli endpoint appropriata",
}


SCOPE_LABELS = {
    "presenza dell'inventario strutturato dei servizi erogati da fornitori": "la presenza dell'inventario strutturato dei servizi erogati da fornitori",
    "aggiornamento sostanziale e completezza dei rapporti di fornitura": "l'aggiornamento sostanziale e la completezza dei rapporti di fornitura",
    "uso dichiarato dei canali monitorati per identificare vulnerabilità": "l'uso dichiarato dei canali monitorati per identificare vulnerabilità",
    "completezza sostanziale dell'identificazione su ogni tecnologia": "la completezza sostanziale dell'identificazione su ogni tecnologia",
    "presenza, freschezza e struttura della relazione di valutazione delle vulnerabilità": "la presenza, la freschezza e la struttura della relazione di valutazione delle vulnerabilità",
    "profondità tecnica e adeguatezza sostanziale di valutazioni e test tecnici approfonditi": "la profondità tecnica e l'adeguatezza sostanziale delle valutazioni e dei test tecnici approfonditi",
    "monitoraggio e stato tecnico di rimozione o mitigazione": "il monitoraggio e lo stato tecnico di rimozione o mitigazione",
    "piano organizzativo, ruoli e approvazione dell'organo direttivo": "il piano organizzativo, i ruoli e l'approvazione dell'organo direttivo",
    "monitoraggio strutturato dei canali dei fornitori critici": "il monitoraggio strutturato dei canali dei fornitori critici",
    "adeguatezza sostanziale della selezione dei fornitori e delle risposte": "l'adeguatezza sostanziale della selezione dei fornitori e delle risposte",
    "autenticazione a più fattori per utenze privilegiate o remote selezionate distinguendo stati noti, sconosciuti e contrastanti": "l'autenticazione a più fattori per le utenze privilegiate o remote selezionate distinguendo stati noti, sconosciuti e contrastanti",
    "giudizio complessivo di adeguatezza dell'autenticazione rispetto al rischio": "il giudizio complessivo di adeguatezza dell'autenticazione rispetto al rischio",
    "presenza e validità dell'evidenza di protezione fisica": "la presenza e la validità dell'evidenza di protezione fisica",
    "adeguatezza sostanziale delle misure fisiche": "l'adeguatezza sostanziale delle misure fisiche",
    "configurazione crittografica dei servizi internet censiti": "la configurazione crittografica dei servizi Internet censiti",
    "evidenze strutturate di manutenzione e dismissione sicura": "le evidenze strutturate di manutenzione e dismissione sicura",
    "adeguatezza sostanziale delle procedure di trasferimento e dismissione": "l'adeguatezza sostanziale delle procedure di trasferimento e dismissione",
}


PURPOSE_BY_CONTROL = {
    "CTRL-ID-AM-01": "la presenza del sistema NIS rilevante nell'inventario tecnico qualificato",
    "CTRL-ID-AM-02": "il censimento, la versione e l'autorizzazione dei componenti software e dei servizi osservati",
    "CTRL-ID-AM-03-E": "il censimento e l'autorizzazione dei flussi di rete rilevanti per il profilo essenziale",
    "CTRL-ID-AM-04": "il censimento delle dipendenze tecniche dai fornitori",
    "CTRL-ID-RA-01": "il monitoraggio delle fonti informative pertinenti per identificare le vulnerabilità",
    "CTRL-ID-RA-01-E": "lo svolgimento delle attività aggiuntive di valutazione delle vulnerabilità previste per il profilo essenziale",
    "CTRL-ID-RA-08": "il monitoraggio delle fonti informative e il trattamento delle vulnerabilità mediante rimozione o mitigazione; un trattamento ancora in corso non è sufficiente",
    "CTRL-ID-RA-08-E": "il monitoraggio dei canali dei fornitori del software ritenuto critico",
    "CTRL-PR-AA-01": "la presenza di utenze individuali e autorizzate con credenziali gestite",
    "CTRL-PR-AA-03": "l'autenticazione a più fattori (MFA) per le utenze privilegiate o di accesso remoto sui sistemi NIS rilevanti",
    "CTRL-PR-AA-05": "l'applicazione del minimo privilegio e la separazione degli account amministrativi",
    "CTRL-PR-AA-06": "la documentazione delle misure di protezione fisica",
    "CTRL-PR-DS-01": "la cifratura dei supporti rimovibili censiti per l'asset",
    "CTRL-PR-DS-02": "la conformità delle configurazioni osservate alla baseline crittografica versionata",
    "CTRL-PR-DS-11": "la periodicità dei backup rispetto al piano e la presenza di copie offline",
    "CTRL-PR-DS-11-E": "la protezione delle copie e l'esito delle prove periodiche di ripristino",
    "CTRL-PR-PS-01-E": "l'applicazione della baseline tecnica di hardening versionata",
    "CTRL-PR-PS-02": "il supporto del software e il rispetto dei termini di aggiornamento definiti dal piano di rischio",
    "CTRL-PR-PS-02-E": "il collaudo degli aggiornamenti critici secondo il processo approvato",
    "CTRL-PR-PS-03-E": "la documentazione tecnica delle attività di manutenzione e dismissione sicura",
    "CTRL-PR-PS-04": "la registrazione degli eventi rilevanti, la protezione e la centralizzazione dei log e la loro conservazione secondo il piano",
    "CTRL-PR-IR-01": "il censimento degli accessi remoti, la protezione dei relativi canali e la difesa del perimetro di rete",
    "CTRL-PR-IR-03-E": "la configurazione e la manutenzione della capacità di comunicazione di emergenza",
    "CTRL-DE-CM-01": "l'abilitazione, la configurazione e il monitoraggio delle capacità tecniche di rilevamento",
    "CTRL-DE-CM-01-E": "la configurazione delle soglie di rilevamento previste per il profilo essenziale",
    "CTRL-DE-CM-09": "l'abilitazione, la configurazione, la manutenzione e il monitoraggio della protezione degli endpoint",
}


CONTROL_TOPIC_BY_ID = {
    "CTRL-ID-AM-01": "l'inventario hardware",
    "CTRL-ID-AM-02": "l'inventario del software e dei servizi",
    "CTRL-ID-AM-03-E": "il censimento dei flussi di rete",
    "CTRL-ID-AM-04": "il censimento dei servizi dei fornitori",
    "CTRL-ID-RA-01": "la valutazione delle vulnerabilità",
    "CTRL-ID-RA-01-E": "la valutazione approfondita delle vulnerabilità",
    "CTRL-ID-RA-08": "il trattamento delle vulnerabilità",
    "CTRL-ID-RA-08-E": "il monitoraggio dei fornitori del software critico",
    "CTRL-PR-AA-01": "la gestione delle identità e delle credenziali",
    "CTRL-PR-AA-03": "l'autenticazione a più fattori (MFA)",
    "CTRL-PR-AA-05": "il minimo privilegio e gli account amministrativi",
    "CTRL-PR-AA-06": "la protezione fisica",
    "CTRL-PR-DS-01": "la protezione dei dati a riposo",
    "CTRL-PR-DS-02": "la protezione dei dati in transito",
    "CTRL-PR-DS-11": "il backup e il ripristino",
    "CTRL-PR-DS-11-E": "la protezione e il collaudo dei backup",
    "CTRL-PR-PS-01-E": "l'hardening dei sistemi",
    "CTRL-PR-PS-02": "il supporto e l'aggiornamento del software",
    "CTRL-PR-PS-02-E": "il collaudo degli aggiornamenti critici",
    "CTRL-PR-PS-03-E": "la manutenzione e la dismissione sicura",
    "CTRL-PR-PS-04": "il logging di sicurezza",
    "CTRL-PR-IR-01": "gli accessi remoti e il firewall",
    "CTRL-PR-IR-03-E": "le comunicazioni di emergenza",
    "CTRL-DE-CM-01": "il monitoraggio di rete e degli accessi",
    "CTRL-DE-CM-01-E": "le soglie di rilevamento delle anomalie",
    "CTRL-DE-CM-09": "la protezione degli endpoint",
}


SUCCESS_BY_CONTROL = {
    "CTRL-ID-AM-01": "l'inventario hardware dell'asset risulta completo",
    "CTRL-ID-AM-02": "l'asset, i servizi e i componenti software richiesti risultano censiti e autorizzati",
    "CTRL-ID-AM-03-E": "i flussi di rete pertinenti risultano censiti e autorizzati",
    "CTRL-ID-AM-04": "i servizi erogati da fornitori risultano censiti nell'inventario tecnico",
    "CTRL-ID-RA-01": "le fonti informative pertinenti alle vulnerabilità risultano monitorate",
    "CTRL-ID-RA-01-E": "risultano svolte le attività aggiuntive di valutazione delle vulnerabilità",
    "CTRL-ID-RA-08": "le vulnerabilità considerate risultano rimosse o mitigate e le fonti pertinenti monitorate",
    "CTRL-ID-RA-08-E": "risultano monitorati i canali dei fornitori del software critico",
    "CTRL-PR-AA-01": "le utenze considerate risultano individuali, autorizzate e soggette a gestione delle credenziali",
    "CTRL-PR-AA-03": "le utenze privilegiate o remote considerate dispongono dell'autenticazione a più fattori",
    "CTRL-PR-AA-05": "le utenze rispettano il minimo privilegio e quelle amministrative sono separate dagli account ordinari",
    "CTRL-PR-AA-06": "la protezione fisica dell'asset risulta documentata",
    "CTRL-PR-DS-01": "i supporti rimovibili censiti risultano cifrati",
    "CTRL-PR-DS-02": "le comunicazioni considerate risultano cifrate secondo la configurazione ammessa",
    "CTRL-PR-DS-11": "i backup rispettano il piano e comprendono copie offline",
    "CTRL-PR-DS-11-E": "le copie di backup risultano protette e le prove di ripristino hanno avuto esito positivo",
    "CTRL-PR-PS-01-E": "la baseline tecnica di hardening risulta applicata",
    "CTRL-PR-PS-02": "i componenti software risultano supportati e aggiornati nei termini del piano di rischio",
    "CTRL-PR-PS-02-E": "gli aggiornamenti critici risultano testati secondo il processo previsto",
    "CTRL-PR-PS-03-E": "le attività di manutenzione e dismissione sicura risultano documentate",
    "CTRL-PR-PS-04": "gli accessi amministrativi e remoti sono registrati e i log richiesti risultano protetti e conservati secondo il piano",
    "CTRL-PR-IR-01": "gli accessi remoti risultano censiti e protetti e il firewall è attivo",
    "CTRL-PR-IR-03-E": "la capacità di comunicazione di emergenza risulta configurata e mantenuta",
    "CTRL-DE-CM-01": "le capacità di rilevamento considerate risultano abilitate, configurate e monitorate",
    "CTRL-DE-CM-01-E": "le soglie per il rilevamento delle anomalie risultano configurate",
    "CTRL-DE-CM-09": "la protezione degli endpoint risulta abilitata, configurata, mantenuta e monitorata",
}


NON_APPLICABILITY_LABELS = {
    "nis_relevance_excluded": "rilevanza NIS conosciuta e negativa",
    "profile_excluded": "regole escluse dal profilo ACN",
    "asset_type_excluded": "tipo di asset non pertinente",
    "services_absent": "assenza dei servizi richiesti dal controllo",
    "service_exposure_excluded": "servizi non esposti nel contesto richiesto",
    "removable_media_excluded": "assenza di supporti rimovibili",
}


class _MainReport:
    def __init__(self) -> None:
        self.lines: list[str] = []
        self.number = 0

    def section(self, title: str) -> None:
        self.number += 1
        self.lines += ["", f"## {self.number}. {title}", ""]

    def paragraph(self, text: str) -> None:
        self.lines += [text, ""]


def render_main_report(report: Mapping[str, Any]) -> str:
    """Restituisce il solo report discorsivo destinato alla lettura umana."""
    document = _MainReport()
    organization = report["organization"]
    summary = report["summary"]
    document.lines = [
        f"# Report di valutazione tecnica — {_value(organization.get('name'))}"
    ]

    document.section("Scenario")
    observed = int(summary["assets_observed"])
    observed_clause = (
        "Non è stato osservato alcun asset"
        if observed == 0
        else f"{'È stato osservato' if observed == 1 else 'Sono stati osservati'} {_quantity(observed, 'asset', 'asset')}"
    )
    document.paragraph(
        f"La valutazione dello scenario `{_text(report['assessment_id'])}` riguarda "
        f"{_value(organization.get('name'))}, con profilo ACN **{_value(report['framework_metadata'].get('acn_profile'))}**, "
        f"alla data del {_date(report.get('assessment_date'))}. {observed_clause}; "
        f"{_quantity(summary['assets_analyzed'], 'asset', 'asset')} "
        f"{'è rilevante' if summary['assets_analyzed'] < 2 else 'sono rilevanti'} per il perimetro NIS."
    )

    document.section("Sintesi della valutazione")
    document.paragraph(_summary_counts(report))
    document.paragraph(_summary_areas(report))
    if report["action_plan"]:
        document.paragraph(_first_priority_summary(report, report["action_plan"][0]))
    document.lines += [
        "| Esito | Numero |",
        "| --- | ---: |",
        f"| Soddisfatti | {summary['compliant']} |",
        f"| Non soddisfatti | {summary['non_compliant']} |",
        f"| Non verificabili | {summary['not_verifiable_controls']} |",
        f"| Non applicabili | {summary['not_applicable_controls']} |",
        f"| Revisione manuale | {summary['manual_review_required']} |",
        "",
        "I conteggi si riferiscono alle valutazioni asset-controllo e non rappresentano una percentuale complessiva di conformità NIS2.",
        "",
    ]

    document.section("Analisi per asset")
    overviews = sorted(
        report["asset_overviews"],
        key=lambda item: (item["asset"].get("nis_relevant") is not True, str(item["asset"].get("id"))),
    )
    for overview in overviews:
        document.lines += _asset_paragraphs(overview)

    non_compliant = _status_results(report, "non_compliant")
    if non_compliant:
        document.section("Controlli non soddisfatti")
        for result in non_compliant:
            document.lines += _non_compliant_control(result)

    not_verifiable = _status_results(report, "not_verifiable")
    if not_verifiable:
        document.section("Controlli non verificabili")
        for result in not_verifiable:
            document.lines += _not_verifiable_control(result)

    if report["manual_reviews"]:
        document.section("Revisioni manuali di governance")
        for result in report["manual_reviews"]:
            document.lines += _manual_review_control(result)

    compliant = _status_results(report, "compliant")
    if compliant:
        document.section("Controlli soddisfatti")
        for result in compliant:
            document.lines += _compliant_control(result)

    if report["excluded_controls"]:
        document.section("Controlli non applicabili")
        document.lines += _non_applicable_paragraphs(
            report["excluded_controls"],
            profile=_value(report["framework_metadata"].get("acn_profile")),
        )

    document.section("Priorità di intervento")
    document.lines += _priorities(report)

    document.section("Perimetro e limiti")
    document.paragraph(_limits(report))

    return "\n".join(document.lines).rstrip() + "\n"


def _summary_counts(report: Mapping[str, Any]) -> str:
    summary = report["summary"]
    applicable = int(summary["applicable_controls"])
    applicable_clause = (
        "Nessun controllo è applicabile"
        if applicable == 0
        else f"{'È applicabile' if applicable == 1 else 'Sono applicabili'} "
        f"{_quantity(applicable, 'controllo', 'controlli')}"
    )
    manual = int(summary["manual_review_required"])
    manual_clause = (
        "nessun risultato richiede una revisione manuale di governance."
        if manual == 0
        else f"{_quantity(manual, 'risultato', 'risultati')} "
        f"{'richiede' if manual == 1 else 'richiedono'} una revisione manuale di governance."
    )
    excluded = int(summary["not_applicable_controls"])
    excluded_clause = (
        "non risultano valutazioni non applicabili"
        if excluded == 0
        else f"{_quantity(excluded, 'valutazione', 'valutazioni', feminine=True).capitalize()} "
        f"{'non è applicabile' if excluded == 1 else 'non sono applicabili'}"
    )
    return (
        f"{applicable_clause}: "
        f"{_status_reference(summary['compliant'], 'risulta soddisfatto', 'risultano soddisfatti')}, "
        f"{_non_compliant_reference(summary['non_compliant'], report_style=True)} "
        f"e {_not_verifiable_reference(summary['not_verifiable_controls'])}. "
        f"{excluded_clause}; "
        f"{manual_clause}"
    )


def _summary_areas(report: Mapping[str, Any]) -> str:
    problem = sorted(
        (
            counts.get("non_compliant", 0) + counts.get("not_verifiable", 0),
            str(area),
        )
        for area, counts in report["results_by_area"].items()
    )
    problem_names = [
        AREA_LABELS.get(area, area.replace("_", " "))
        for count, area in sorted(problem, key=lambda item: (-item[0], item[1]))[:3]
        if count
    ]
    adequate_names = _unique(
        AREA_LABELS.get(
            str(result["context"]["control"].get("technical_area")),
            str(result["context"]["control"].get("technical_area", "")).replace("_", " "),
        )
        for result in report["assessment_results"]
        if result.get("technical_status") == "compliant"
    )
    adequate = (
        "I controlli soddisfatti riguardano " + _join(adequate_names) + ". "
        if adequate_names
        else ""
    )
    problems = (
        "Gli scostamenti e le lacune informative interessano soprattutto "
        + _join(problem_names)
        + "."
        if problem_names
        else "Non emergono scostamenti o lacune informative."
    )
    return adequate + problems


def _asset_paragraphs(overview: Mapping[str, Any]) -> list[str]:
    asset = overview["asset"]
    name = _value(asset.get("name"))
    asset_id = _text(asset.get("id"))
    if asset.get("nis_relevant") is False:
        return [
            f"### {name} (`{asset_id}`)",
            "",
            "L'asset è escluso dalla valutazione tecnica perché la sua rilevanza NIS è conosciuta e negativa.",
            "",
        ]
    counts = overview["status_counts"]
    applicable = len(overview["applicable_results"])
    issue_names = _unique(
        _action_topic(item) for item in overview["priority_actions"]
    )[:3]
    paragraph = (
        f"Per {name} {'è applicabile' if applicable == 1 else 'sono applicabili'} "
        f"{_quantity(applicable, 'controllo', 'controlli')}: "
        f"{_status_reference(counts.get('compliant', 0), 'è soddisfatto', 'sono soddisfatti')}, "
        f"{_non_compliant_reference(counts.get('non_compliant', 0))} "
        f"e {_not_verifiable_reference(counts.get('not_verifiable', 0))}."
    )
    if issue_names:
        paragraph += " Nell'ordine operativo, i primi problemi riguardano " + _join(issue_names) + "."
    return [f"### {name} (`{asset_id}`)", "", paragraph, ""]


def _non_compliant_control(result: Mapping[str, Any]) -> list[str]:
    title = _control_heading(result)
    issues = _violation_sentences(result)
    evidence = _decision_basis(result)
    coverage = _coverage_limit(result)
    action = _corrective_action(result, len(issues))
    gap = _coexisting_gap_sentence(result)
    topic = CONTROL_TOPIC_BY_ID.get(
        str(result.get("control_id")),
        "il controllo " + _lower(_value(result["context"]["control"].get("title"))),
    )
    if issues:
        issue_text = _join([_lower(_sentence_fragment(item)) for item in issues])
        opening = f"Il controllo riguardante {topic} non è soddisfatto perché {issue_text}."
    else:
        opening = f"Il controllo riguardante {topic} non è soddisfatto nelle condizioni previste."
    sentences = [opening]
    if gap:
        sentences.append(gap)
    if evidence:
        sentences.append(evidence)
    if coverage:
        sentences.append(coverage)
    if action:
        sentences.append(action)
    return [title, "", " ".join(_sentence(item) for item in sentences), ""]


def _not_verifiable_control(result: Mapping[str, Any]) -> list[str]:
    title = _control_heading(result)
    sentences = [_purpose(result), *_gap_sentences(result)]
    discarded = _discarded_evidence_sentences(result)
    sentences.extend(discarded)
    sentences.append("Finché la lacuna permane, il controllo non è verificabile.")
    request = _information_request(result)
    if request:
        sentences.append(request)
    return [title, "", " ".join(_sentence(item) for item in sentences), ""]


def _manual_review_control(result: Mapping[str, Any]) -> list[str]:
    technical = _value(result.get("technical_status"))
    sentences = [
        f"L'esito tecnico del controllo resta **{technical}** e non viene modificato dalla revisione di governance."
    ]
    exception = result.get("technical_exception_details") or {}
    risks = result.get("accepted_risk_details") or []
    if exception:
        sentences.append(
            f"È presente la deroga `{_text(exception.get('id'))}`. La motivazione registrata è: {_value(exception.get('rationale'))}"
        )
        sentences.append(
            f"La misura compensativa registrata è {_lower(_value(exception.get('compensating_measure')))}"
        )
        sentences.append(
            f"Devono essere riesaminati l'approvazione {_value(exception.get('approval_reference'))}, il rischio residuo di livello {_risk_value(exception.get('residual_risk'))} e la validità fino al {_date(exception.get('valid_until'))}."
        )
    elif risks:
        names = [f"`{_text(item.get('id'))}`" for item in risks]
        sentences.append(
            "È registrato un rischio accettato per " + _join(names) + ", che richiede una verifica manuale di ambito, approvazione, durata e stato del trattamento."
        )
    elif result.get("conflicting_information"):
        sentences.append(
            "La revisione è richiesta perché fonti considerate nella decisione forniscono informazioni contrastanti; occorre stabilire quale fonte sia attendibile e correggere l'altra."
        )
    else:
        sentences.append(
            "Il risultato richiede una valutazione manuale del contesto di governance registrato dal motore."
        )
    return [_control_heading(result), "", " ".join(_sentence(item) for item in sentences), ""]


def _compliant_control(result: Mapping[str, Any]) -> list[str]:
    condition = SUCCESS_BY_CONTROL.get(
        str(result.get("control_id")),
        "le condizioni tecniche previste dalla regola risultano soddisfatte",
    )
    basis = _evidence_basis(result)
    opening = _sentence_fragment(condition).capitalize()
    if basis:
        opening += f" {basis}"
    coverage = result["context"]["rule"].get("coverage", {})
    if coverage.get("level") == "partial":
        verified = _scope_with_article(coverage.get("verified_scope"))
        unverified = _scope_with_article(coverage.get("unverified_scope"))
        close = f"Il controllo è soddisfatto limitatamente {_prepositional_scope(verified)}"
        if unverified:
            close += f", mentre non valuta {unverified}"
        paragraph = " ".join((_sentence(opening), _sentence(close)))
    else:
        paragraph = _sentence(
            opening
            + "; il controllo è pertanto soddisfatto per tutte le condizioni tecniche previste dalla regola"
        )
    return [
        _control_heading(result),
        "",
        paragraph,
        "",
    ]


def _purpose(result: Mapping[str, Any]) -> str:
    control_id = str(result.get("control_id"))
    if control_id in PURPOSE_BY_CONTROL:
        return f"Il controllo verifica {PURPOSE_BY_CONTROL[control_id]}."
    description = str(
        result["context"]["rule"].get("description")
        or result["context"]["control"].get("description")
        or "le condizioni tecniche previste"
    ).strip()
    description = description.removeprefix("Verifica ").removeprefix("Valuta ")
    description = description.removeprefix("Confronta ")
    replacements = {
        "remediation o mitigazione": "la rimozione o la mitigazione delle vulnerabilità",
        "in corso non è soddisfacimento": "un trattamento ancora in corso non è sufficiente",
        "MFA": "l'autenticazione a più fattori (MFA)",
        "retention": "conservazione",
    }
    for source, target in replacements.items():
        description = description.replace(source, target)
    return "Il controllo verifica " + _lower(description)


def _violation_sentences(result: Mapping[str, Any]) -> list[str]:
    facts = [
        fact
        for fact in result.get("evaluated_facts", [])
        if fact.get("comparison_result") is False and fact.get("mandatory", True)
    ]
    sentences: list[str] = []
    mfa = [fact for fact in facts if _field(fact) == "mfa_enabled"]
    if mfa:
        failed = [_entity(fact) for fact in mfa]
        passed = [
            _entity(fact)
            for fact in result.get("evaluated_facts", [])
            if _field(fact) == "mfa_enabled" and fact.get("comparison_result") is True
        ]
        if passed:
            sentences.append(
                f"{_quantity(len(passed), 'utenza pertinente', 'utenze pertinenti', feminine=True).capitalize()} "
                f"{'dispone' if len(passed) == 1 else 'dispongono'} dell'autenticazione a più fattori, mentre {_entities(failed)} ne è priva."
            )
        else:
            sentences.append(f"{_entities(failed).capitalize()} non dispone dell'autenticazione a più fattori.")
        facts = [fact for fact in facts if _field(fact) != "mfa_enabled"]
    sentences.extend(_issue_sentence(fact) for fact in facts)
    return _unique(sentences)


def _issue_sentence(fact: Mapping[str, Any]) -> str:
    field = _field(fact)
    entity = _entity(fact)
    kind = str(fact.get("path") or "").split(".", maxsplit=1)[0]
    value_status = fact.get("value_status")
    if value_status != "known":
        return _unknown_fact_sentence(field, entity)
    templates = {
        "provider_services_inventory_complete": "L'inventario dei servizi erogati dai fornitori è incompleto.",
        "vulnerability_advisories_monitored": "Il monitoraggio delle fonti pertinenti alle vulnerabilità non è attivo.",
        "extended_vulnerability_assessment_performed": "Non risulta eseguita la valutazione approfondita delle vulnerabilità richiesta.",
        "credentials_managed": f"Le credenziali dell'utenza `{entity}` non risultano gestite secondo le condizioni previste.",
        "least_privilege": f"All'utenza `{entity}` non è applicato il minimo privilegio.",
        "separate_admin_account": f"L'utenza amministrativa `{entity}` non dispone di un account separato per le sole attività privilegiate.",
        "encrypted": f"Il servizio `{entity}` trasmette dati senza la cifratura richiesta.",
        "frequency_within_plan": f"Il backup `{entity}` non rispetta la frequenza stabilita dal piano.",
        "offline_copy": f"Per il backup `{entity}` non risulta disponibile la copia offline richiesta.",
        "protected_copy": f"La copia di backup `{entity}` non risulta protetta.",
        "restore_test_successful": f"La prova di ripristino del backup `{entity}` non ha avuto esito positivo.",
        "hardening_baseline_applied": "La baseline tecnica di hardening non risulta applicata all'asset.",
        "critical_update_tested": f"Gli aggiornamenti critici del componente `{entity}` non risultano testati.",
        "maintenance_logged": "Le attività di manutenzione dell'asset non risultano registrate.",
        "secure_disposal_documented": "La dismissione sicura dell'asset non risulta documentata.",
        "admin_remote_access_logging": "Gli accessi amministrativi e remoti non risultano registrati.",
        "logs_protected": "I log di sicurezza non risultano protetti.",
        "log_retention_within_plan": "La conservazione dei log non rispetta il piano definito.",
        "remote_access_registry_complete": "Il registro degli accessi remoti è incompleto.",
        "remote_access_protected": "Gli accessi remoti non risultano adeguatamente protetti.",
        "firewall_enabled": "Il firewall richiesto non risulta attivo.",
        "anomaly_thresholds_configured": "Le soglie per il rilevamento delle anomalie non risultano configurate.",
        "hardware_inventory_complete": "L'inventario hardware dell'asset è incompleto.",
    }
    if field == "authorized":
        subject = {"NetworkFlow": "Il flusso di rete", "Service": "Il servizio", "Account": "L'utenza"}.get(kind, "L'entità")
        return f"{subject} `{entity}` non risulta autorizzato nel contesto valutato."
    if field == "remediation_status":
        return f"La vulnerabilità `{entity}` è ancora aperta o in corso di trattamento e non risulta rimossa o mitigata."
    if field == "security_update_status":
        return f"Il componente software `{entity}` ha superato il termine di aggiornamento previsto dal piano di rischio."
    if field == "support_status":
        return f"Il componente software `{entity}` non è più supportato."
    if field == "tls_versions":
        return f"Il servizio `{entity}` utilizza una versione del protocollo di cifratura non ammessa dalla baseline tecnica."
    if field in {"enabled", "configured", "maintained", "monitored"}:
        subject = "La capacità di sicurezza" if kind == "SecurityCapability" else "La misura"
        labels = {
            "enabled": "non risulta attiva",
            "configured": "non risulta configurata",
            "maintained": "non risulta mantenuta",
            "monitored": "non risulta monitorata",
        }
        return f"{subject} `{entity}` {labels[field]}."
    if field in templates:
        return templates[field]
    return f"La proprietà tecnica relativa a {_readable_field(field)} non soddisfa la condizione prevista."


def _unknown_fact_sentence(field: str, entity: str) -> str:
    if field == "vulnerability_advisories_monitored":
        return "Non è disponibile un dato conclusivo sul monitoraggio delle fonti pertinenti alle vulnerabilità."
    return f"Per `{entity}` non è disponibile un dato conclusivo relativo a {_readable_field(field)}."


def _gap_sentences(result: Mapping[str, Any]) -> list[str]:
    missing = [str(item) for item in result.get("missing_information", [])]
    sentences: list[str] = []
    joined = " ".join(missing)
    if "DataObject.inventory_status" in joined:
        sentences.append(
            "Non è nota la completezza dell'inventario dei dati e dei supporti rimovibili; senza questa informazione non è possibile stabilire se tutti gli elementi da proteggere siano stati considerati."
        )
    if "provider_services_inventory_complete" in joined:
        sentences.append(
            "Non è stato dichiarato se l'inventario dei servizi erogati dai fornitori sia completo."
        )
    if "vulnerability_advisories_monitored" in joined:
        sentences.append(
            "Il dato sul monitoraggio delle fonti pertinenti alle vulnerabilità non è stato raccolto."
        )
    if "critical_software_supplier_channels_monitored" in joined:
        sentences.append(
            "Non è stato raccolto lo stato del monitoraggio dei canali dei fornitori del software critico."
        )
    if "physical_protection_documented" in joined:
        sentences.append(
            "Non è stato dichiarato se le misure di protezione fisica dell'asset siano documentate."
        )
    evidence_missing = [item for item in missing if item.lower().startswith("evidence.")]
    if evidence_missing:
        sentences.append(
            "Manca inoltre l'evidenza richiesta per sostenere la verifica con dati ammissibili e aggiornati."
        )
    if result.get("conflicting_information"):
        sentences.append(
            "Le fonti ammesse forniscono valori contrastanti e il criterio decisionale non consente di stabilire quale debba prevalere."
        )
    undetermined = [
        str(item.get("entity_id"))
        for item in result.get("selector_decisions", [])
        if item.get("status") == "undetermined"
    ]
    if undetermined:
        sentences.append(
            f"Lo stato di {_entities(undetermined)} è indeterminato e impedisce di completare la valutazione della collezione."
        )
    applicability = result.get("applicability_details") or {}
    if applicability.get("status") == "undetermined" and not sentences:
        sentences.append(
            "Manca l'informazione necessaria per determinare se il controllo sia applicabile all'asset."
        )
    if not sentences:
        sentences.append(
            "Le informazioni disponibili non sono sufficienti per stabilire se le condizioni del controllo siano soddisfatte."
        )
    return _unique(sentences)


def _discarded_evidence_sentences(result: Mapping[str, Any]) -> list[str]:
    reasons = [
        str(item.get("reason") or item.get("reason_code") or "")
        for item in result.get("decision_trace", {}).get("discarded_evidence", [])
        if isinstance(item, Mapping)
    ]
    text = " ".join(reasons).lower()
    sentences: list[str] = []
    if "non corrente" in text or "scadut" in text:
        sentences.append("L'evidenza disponibile è scaduta o non sufficientemente recente e non può sostenere la decisione.")
    if "associazione" in text:
        sentences.append("L'evidenza disponibile è associata a un asset o a un controllo diverso e non è utilizzabile in questa verifica.")
    if "policy" in text or "provenienza" in text:
        sentences.append("L'evidenza disponibile non rispetta i requisiti di ammissibilità o provenienza stabiliti per la verifica.")
    return sentences


def _information_request(result: Mapping[str, Any]) -> str:
    missing = " ".join(str(item) for item in result.get("missing_information", []))
    unknown_support = [
        fact
        for fact in result.get("evaluated_facts", [])
        if _field(fact) == "support_status" and fact.get("value_status") != "known"
    ]
    if unknown_support:
        count = len(_unique(_entity(fact) for fact in unknown_support))
        subject = "del componente software" if count == 1 else "dei componenti software interessati"
        return f"Occorre verificare lo stato di supporto {subject} prima di definire l'intervento tecnico."
    if "DataObject.inventory_status" in missing:
        return "Occorre completare o confermare l'inventario dei dati e dei supporti rimovibili; una volta accertato l'ambito, sarà possibile verificarne la cifratura."
    if "provider_services_inventory_complete" in missing:
        return "Occorre confermare la completezza dell'inventario dei servizi dei fornitori e acquisire l'evidenza richiesta."
    if "vulnerability_advisories_monitored" in missing:
        return "Occorre acquisire lo stato del monitoraggio delle fonti pertinenti e la relativa evidenza."
    if "critical_software_supplier_channels_monitored" in missing:
        return "Occorre acquisire lo stato del monitoraggio dei canali dei fornitori critici e la relativa evidenza."
    if "physical_protection_documented" in missing:
        return "Occorre acquisire documentazione aggiornata sulle misure di protezione fisica dell'asset."
    if result.get("conflicting_information"):
        return "Occorre risolvere il conflitto tra le fonti, identificare quella autoritativa e ripetere la verifica."
    discarded = " ".join(
        str(item.get("reason") or item.get("reason_code") or "")
        for item in result.get("decision_trace", {}).get("discarded_evidence", [])
        if isinstance(item, Mapping)
    ).lower()
    if "non corrente" in discarded or "scadut" in discarded:
        return "Occorre aggiornare l'evidenza scaduta o acquisirne una corrente, quindi ripetere la verifica."
    if "associazione" in discarded:
        return "Occorre acquisire un'evidenza correttamente associata all'asset e al controllo, quindi ripetere la verifica."
    if "policy" in discarded or "provenienza" in discarded:
        return "Occorre acquisire un'evidenza conforme ai requisiti di ammissibilità e provenienza, quindi ripetere la verifica."
    applicability = result.get("applicability_details") or {}
    if applicability.get("status") == "undetermined":
        return "Occorre acquisire le informazioni mancanti per determinare l'applicabilità del controllo e solo in seguito eseguirne la verifica tecnica."
    evidence_missing = [
        item for item in result.get("missing_information", [])
        if str(item).lower().startswith("evidence.")
    ]
    if evidence_missing:
        return "Occorre acquisire un'evidenza ammissibile e aggiornata, quindi ripetere la verifica."
    actions = _unique(result.get("information_actions", []))
    return _sentence(actions[0]) if actions else "Occorre acquisire le informazioni mancanti e ripetere la verifica."


def _coexisting_gap_sentence(result: Mapping[str, Any]) -> str:
    if not result.get("missing_information") and not result.get("conflicting_information"):
        return ""
    gaps = _gap_sentences(result)
    detail = _lower(gaps[0])
    if detail.startswith("manca inoltre "):
        return "Resta inoltre da acquisire " + detail.removeprefix("manca inoltre ")
    return "Resta inoltre una lacuna informativa: " + detail


def _evidence_basis(result: Mapping[str, Any]) -> str:
    evidences = result.get("evidence_details", [])
    if not evidences:
        return ""
    sources = _unique(_source_label(item.get("source")) for item in evidences)
    if sources:
        return "sulla base dei dati acquisiti " + _join(sources)
    titles = _unique(item.get("title") for item in evidences)
    if len(titles) == 1:
        return f"sulla base dell'evidenza {_join(titles)}"
    return f"sulla base delle evidenze {_join(titles)}"


def _decision_basis(result: Mapping[str, Any]) -> str:
    evidences = result.get("evidence_details", [])
    sources = _unique(_source_label(item.get("source")) for item in evidences)
    if sources:
        return _sentence("La decisione si basa sui dati acquisiti " + _join(sources))
    titles = _unique(item.get("title") for item in evidences)
    if len(titles) == 1:
        return _sentence("La decisione si basa sull'evidenza " + titles[0])
    if titles:
        return _sentence("La decisione si basa sulle evidenze " + _join(titles))
    return ""


def _coverage_limit(result: Mapping[str, Any]) -> str:
    coverage = result["context"]["rule"].get("coverage", {})
    level = coverage.get("level")
    if level == "partial":
        verified = _scope_with_article(coverage.get("verified_scope"))
        unverified = _scope_with_article(coverage.get("unverified_scope"))
        if unverified:
            return f"La verifica riguarda {verified}, mentre non valuta {unverified}."
        return f"La verifica è limitata a {verified}."
    return ""


def _corrective_action(result: Mapping[str, Any], issue_count: int) -> str:
    actions = _unique(
        [result.get("recommendation"), *result.get("technical_remediations", [])]
    )
    if not actions:
        return ""
    subject = "lo scostamento" if issue_count == 1 else "gli scostamenti"
    action = _reporting_action(result, actions[0])
    return f"Per correggere {subject} occorre " + _lower(action)


def _reporting_action(result: Mapping[str, Any], fallback: Any) -> str:
    control_id = str(result.get("control_id"))
    if control_id == "CTRL-PR-PS-02":
        action = _software_action(result)
        if action:
            return action
    if control_id == "CTRL-ID-RA-08":
        vulnerabilities = _unique(
            _entity(fact)
            for fact in result.get("evaluated_facts", [])
            if _field(fact) == "remediation_status"
            and fact.get("comparison_result") is False
        )
        if len(vulnerabilities) == 1:
            return "Rimuovere o mitigare la vulnerabilità e registrare l'eventuale rischio residuo."
        if vulnerabilities:
            return "Rimuovere o mitigare le vulnerabilità interessate e registrare gli eventuali rischi residui."
    return _human_action(fallback)


def _software_action(result: Mapping[str, Any]) -> str:
    facts = result.get("evaluated_facts", [])
    overdue = _unique(
        _entity(fact)
        for fact in facts
        if _field(fact) == "security_update_status"
        and fact.get("comparison_result") is False
    )
    unsupported = _unique(
        _entity(fact)
        for fact in facts
        if _field(fact) == "support_status" and fact.get("comparison_result") is False
    )
    unknown_support = _unique(
        _entity(fact)
        for fact in facts
        if _field(fact) == "support_status" and fact.get("value_status") != "known"
    )
    actions: list[str] = []
    if overdue:
        if len(overdue) == 1:
            actions.append(
                "Aggiornare il componente software e ricondurne la gestione entro i termini previsti dal piano di rischio."
            )
        else:
            actions.append(
                "Aggiornare i componenti software interessati e ricondurne la gestione entro i termini previsti dal piano di rischio."
            )
    if unsupported:
        if len(unsupported) == 1:
            replacement = "Sostituire o migrare il componente software fuori supporto."
        else:
            replacement = "Sostituire o migrare i componenti software fuori supporto."
        actions.append("Occorre inoltre " + _lower(replacement) if actions else replacement)
    if unknown_support:
        if len(unknown_support) == 1:
            actions.append("Verificare inoltre lo stato di supporto del componente software.")
        else:
            actions.append("Verificare inoltre lo stato di supporto dei componenti software interessati.")
    return " ".join(actions)


def _non_applicable_paragraphs(
    excluded: Sequence[Mapping[str, Any]], *, profile: str
) -> list[str]:
    groups: dict[str, list[Mapping[str, Any]]] = {}
    for item in excluded:
        groups.setdefault(str(item.get("reason_code") or "other"), []).append(item)
    lines: list[str] = []
    for code, items in sorted(groups.items(), key=lambda pair: _non_applicability_order(pair[0])):
        controls = _unique(item.get("control_title") for item in items)
        assets = _unique(item.get("asset_name") for item in items)
        if code == "nis_relevance_excluded":
            asset_subject = (
                f"l'asset {_join(assets)}"
                if len(assets) == 1
                else f"gli asset {_join(assets)}"
            )
            paragraph = (
                f"Per {asset_subject} {'non è applicabile' if len(controls) == 1 else 'non sono applicabili'} "
                f"{_quantity(len(controls), 'controllo', 'controlli')}, poiché "
                f"{'è dichiarato' if len(assets) == 1 else 'sono dichiarati'} "
                f"{'esterno' if len(assets) == 1 else 'esterni'} al perimetro NIS."
            )
        elif code == "profile_excluded":
            evaluations = _quantity(
                len(items), "valutazione", "valutazioni", feminine=True
            )
            if len(assets) == 1:
                asset_scope = f"per l'asset {_join(assets)}"
            elif len(assets) == 2:
                asset_scope = "per entrambi gli asset"
            else:
                asset_scope = f"per {_quantity(len(assets), 'asset', 'asset')}"
            evaluation_subject = (
                "Un'altra valutazione" if len(items) == 1 else f"Altre {evaluations}"
            )
            paragraph = (
                f"{evaluation_subject} {'non è applicabile' if len(items) == 1 else 'non sono applicabili'} perché "
                f"{'riguarda' if len(items) == 1 else 'riguardano'} "
                f"{_quantity(len(controls), 'controllo', 'controlli')} "
                f"{'escluso' if len(controls) == 1 else 'esclusi'} dal profilo ACN {profile} {asset_scope}."
            )
        else:
            cause = NON_APPLICABILITY_LABELS.get(
                code, "un'altra condizione di applicabilità certamente falsa"
            )
            evaluations = _quantity(
                len(items), "valutazione", "valutazioni", feminine=True
            )
            paragraph = (
                f"{evaluations.capitalize()} {'non è applicabile' if len(items) == 1 else 'non sono applicabili'} "
                f"per {cause}; {'riguarda' if len(controls) == 1 else 'riguardano'} "
                f"{_quantity(len(controls), 'controllo', 'controlli')} su {_join(assets)}."
            )
        if len(controls) <= 5:
            label = (
                "Il controllo interessato è "
                if len(controls) == 1
                else "I controlli interessati sono "
            )
            paragraph += " " + label + _join(controls) + "."
        lines += [paragraph, ""]
    return lines


def _non_applicability_order(code: str) -> tuple[int, str]:
    order = [
        "nis_relevance_excluded",
        "profile_excluded",
        "asset_type_excluded",
        "services_absent",
        "service_exposure_excluded",
        "removable_media_excluded",
    ]
    return (order.index(code) if code in order else len(order), code)


def _priorities(report: Mapping[str, Any]) -> list[str]:
    actions = report["action_plan"]
    if not actions:
        return ["Non risultano interventi con priorità operativa calcolata.", ""]
    first_names = _unique(_action_topic(item) for item in actions[:3])
    lines = [
        "Gli interventi prioritari riguardano " + _join(first_names) + ". L'ordine deriva dallo score operativo già calcolato, usato soltanto per ordinare gli interventi: non misura la conformità NIS2 né la gravità normativa.",
        "",
        "| Ordine | Asset | Controllo | Intervento |",
        "| ---: | --- | --- | --- |",
    ]
    for item in actions:
        lines.append(
            f"| {item['rank']} | {_cell(item.get('asset_name'))} | {_cell(item.get('control_title'))} | {_cell(_priority_action(report, item))} |"
        )
    lines.append("")
    return lines


def _first_priority_summary(
    report: Mapping[str, Any], item: Mapping[str, Any]
) -> str:
    topic = CONTROL_TOPIC_BY_ID.get(
        str(_result_for_action(report, item).get("control_id")),
        "il controllo " + _lower(_sentence_fragment(item.get("control_title"))),
    )
    action = _lower(_sentence_fragment(_priority_action(report, item)))
    return (
        f"Il problema complessivamente più urgente riguarda {topic} di "
        f"{_value(item.get('asset_name'))}, per cui occorre {action.removeprefix('occorre ')}."
    )


def _priority_action(report: Mapping[str, Any], item: Mapping[str, Any]) -> str:
    result = _result_for_action(report, item)
    if result.get("technical_status") == "not_verifiable":
        action = _sentence_fragment(_information_request(result))
        return _sentence(action.removeprefix("Occorre ").capitalize())
    return _reporting_action(result, item.get("recommendation"))


def _action_topic(item: Mapping[str, Any]) -> str:
    return CONTROL_TOPIC_BY_ID.get(
        str(item.get("control_id")),
        "il controllo " + _lower(_sentence_fragment(item.get("control_title"))),
    )


def _result_for_action(
    report: Mapping[str, Any], item: Mapping[str, Any]
) -> Mapping[str, Any]:
    result_id = str(item.get("result_id"))
    return next(
        (
            result
            for result in report["assessment_results"]
            if str(result.get("id")) == result_id
        ),
        {},
    )


def _limits(report: Mapping[str, Any]) -> str:
    return (
        "La valutazione riguarda esclusivamente il sottoinsieme di controlli tecnici modellato nel progetto per il profilo ACN "
        f"**{_value(report['framework_metadata'].get('acn_profile'))}** e dipende dai dati acquisiti nel `NormalizedEnvironment` `{_text(report['dataset_id'])}`. "
        "Una copertura parziale limita l'esito alla parte tecnicamente osservabile indicata dalla regola e non lo estende agli aspetti organizzativi o sostanziali non modellati. "
        "Il report non costituisce una certificazione né un'attestazione complessiva di conformità alla NIS2."
    )


def render_technical_attachment(report: Mapping[str, Any]) -> str:
    """Restituisce l'allegato completo di audit separato dal corpo principale."""
    lines = [
        f"# Allegato tecnico — assessment `{_text(report['assessment_id'])}`",
        "",
        "Questo allegato conserva i dati tecnici prodotti dal motore senza reinterpretarli.",
        "",
        "## 1. Tracciabilità dei risultati",
        "",
        "| Risultato | Asset | Controllo | Requisito | Regola/versione | Esito tecnico | Governance | Confidence | Copertura |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for result in report["assessment_results"]:
        coverage = result["traceability"].get("coverage", {})
        lines.append(
            f"| `{_cell(result['id'])}` | `{_cell(result['asset_id'])}` | `{_cell(result['control_id'])}` "
            f"| `{_cell(result['requirement_id'])}` | `{_cell(result['rule_id'])}` / `{_cell(result['rule_version'])}` "
            f"| {_cell(result['technical_status'])} | {_cell(result['governance_status'])} "
            f"| {_cell(result['confidence_level'])} | {_cell(coverage.get('level'))} |"
        )

    lines += ["", "## 2. Condizioni, valori e policy decisionali"]
    for result in report["assessment_results"]:
        lines += [
            "",
            f"### `{_text(result['id'])}` — `{_text(result['asset_id'])}` / `{_text(result['control_id'])}`",
            "",
            f"- Decision policy: `{_text(result.get('decision_policy'))}`",
            f"- Technical status: `{_text(result.get('technical_status'))}`",
            f"- Governance status: `{_text(result.get('governance_status'))}`",
            f"- Reason: {_text(result.get('reason'))}",
            f"- Missing information: {_text(result.get('missing_information'))}",
            f"- Conflicting information: {_text(result.get('conflicting_information'))}",
            "",
            "| Percorso | Richiesto | Osservato | Stato valore | Confronto | Obbligatoria | Provenienza |",
            "| --- | --- | --- | --- | --- | --- | --- |",
        ]
        facts = result.get("evaluated_facts", [])
        if not facts:
            lines.append("| — | — | — | — | — | — | — |")
        for fact in facts:
            lines.append(
                f"| `{_cell(fact.get('path'))}` | `{_cell(fact.get('comparison'))}` "
                f"| `{_cell(json.dumps(fact.get('observed_value'), ensure_ascii=False, default=str))}` "
                f"| `{_cell(fact.get('value_status'))}` | `{_cell(fact.get('comparison_result'))}` "
                f"| `{_cell(fact.get('mandatory'))}` | {_cell(fact.get('provenance_ids'))} |"
            )

    lines += [
        "",
        "## 3. Evidenze ammesse, scartate e provenienza",
        "",
        "### 3.1 Catalogo completo delle evidenze",
        "",
        "| Evidenza | Tipo | Asset/controlli | Fonte | Raccolta | Validità | Reliability | Provenienza |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    evidence_usage = _evidence_usage(report)
    for evidence in report["evidence_catalog"]:
        lines.append(
            f"| {_cell(evidence.get('title'))} (`{_cell(evidence.get('id'))}`) | {_cell(evidence.get('evidence_type'))} "
            f"| {_cell(evidence_usage.get(str(evidence.get('id')), []))} | {_cell(evidence.get('source'))} "
            f"| {_cell(evidence.get('collected_at'))} | {_cell(evidence.get('valid_until'))} "
            f"| {_cell(evidence.get('reliability'))} | {_cell(evidence.get('provenance_ids'))} |"
        )
    lines += [
        "",
        "### 3.2 Evidenze scartate",
        "",
        "| Evidenza | Asset/controllo | Motivo |",
        "| --- | --- | --- |",
    ]
    discarded = _discarded_rows(report)
    if not discarded:
        lines.append("| — | — | Nessuna evidenza scartata registrata |")
    for evidence_id, context, reason in discarded:
        lines.append(f"| `{_cell(evidence_id)}` | {_cell(context)} | {_cell(reason)} |")
    lines += [
        "",
        "### 3.3 Catalogo completo della provenienza",
        "",
        "| Provenienza | Fonte | Tipo/categoria | Raccolta | Metodo | Reliability | Riferimento | Note |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for item in report["provenance_catalog"]:
        lines.append(
            f"| `{_cell(item.get('id'))}` | {_cell(item.get('source'))} "
            f"| {_cell(item.get('source_type'))} / {_cell(item.get('source_category'))} "
            f"| {_cell(item.get('collected_at'))} | {_cell(item.get('method'))} "
            f"| {_cell(item.get('reliability'))} | {_cell(item.get('original_reference'))} "
            f"| {_cell(item.get('notes'))} |"
        )

    lines += [
        "",
        "## 4. Ragioni di non applicabilità",
        "",
        "| Asset/controllo | Reason code | Ragioni | Condizioni valutate |",
        "| --- | --- | --- | --- |",
    ]
    for item in report["excluded_controls"]:
        lines.append(
            f"| `{_cell(item.get('asset_id'))}` / `{_cell(item.get('control_id'))}` "
            f"| `{_cell(item.get('reason_code'))}` | {_cell(item.get('reasons'))} "
            f"| {_cell(item.get('evaluated_conditions'))} |"
        )

    lines += ["", "## 5. Decision trace"]
    for result in report["assessment_results"]:
        lines += [
            "",
            f"### `{_text(result['id'])}`",
            "",
            "```json",
            json.dumps(result.get("decision_trace", {}), ensure_ascii=False, indent=2, sort_keys=True, default=str),
            "```",
        ]

    lines += ["", "## 6. Fatti e contesto strutturato"]
    for result in report["assessment_results"]:
        payload = {
            "assessment_result_id": result["id"],
            "evaluated_facts": result.get("evaluated_facts", []),
            "known_violations": result.get("known_violations", []),
            "recommendation": result.get("recommendation"),
            "technical_remediations": result.get("technical_remediations", []),
            "information_actions": result.get("information_actions", []),
            "selector_decisions": result.get("selector_decisions", []),
            "thresholds_used": result.get("thresholds_used", {}),
            "evidence_details": result.get("evidence_details", []),
            "provenance_details": result.get("provenance_details", []),
            "technical_exception_details": result.get("technical_exception_details"),
            "accepted_risk_details": result.get("accepted_risk_details", []),
        }
        lines += [
            "",
            f"### `{_text(result['id'])}`",
            "",
            "```json",
            json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True, default=str),
            "```",
        ]
    return "\n".join(lines).rstrip() + "\n"


def _evidence_usage(report: Mapping[str, Any]) -> dict[str, list[str]]:
    usage: dict[str, list[str]] = {}
    for result in report["assessment_results"]:
        for evidence_id in result.get("evidence_ids", []):
            usage.setdefault(str(evidence_id), []).append(
                f"{result['asset_id']} / {result['control_id']}"
            )
    return usage


def _discarded_rows(report: Mapping[str, Any]) -> list[tuple[str, str, str]]:
    rows: set[tuple[str, str, str]] = set()
    for item in report.get("rejected_evidences", []):
        rows.add((str(item.get("evidence_id") or "—"), "preflight generale", str(item.get("reason") or "—")))
    for result in report["assessment_results"]:
        for item in result.get("decision_trace", {}).get("discarded_evidence", []):
            if isinstance(item, Mapping):
                rows.add(
                    (
                        str(item.get("evidence_id") or item.get("id") or "—"),
                        f"{result['asset_id']} / {result['control_id']}",
                        str(item.get("reason") or item.get("reason_code") or "—"),
                    )
                )
    return sorted(rows)


def _status_results(report: Mapping[str, Any], status: str) -> list[Mapping[str, Any]]:
    return [item for item in report["assessment_results"] if item["technical_status"] == status]


def _control_heading(result: Mapping[str, Any]) -> str:
    title = _value(result["context"]["control"].get("title"))
    if result.get("control_id") == "CTRL-PR-AA-03":
        title = "Autenticazione a più fattori (MFA)"
    return (
        f"### {title} (`{_text(result['control_id'])}`) — "
        f"{_value(result['context']['asset'].get('name'))}"
    )


def _field(fact: Mapping[str, Any]) -> str:
    return str(fact.get("path") or "").split(".")[-1]


def _entity(fact: Mapping[str, Any]) -> str:
    parts = str(fact.get("path") or "").split(".")
    return parts[-2] if len(parts) >= 3 and parts[0] != "asset" else "l'asset"


def _entities(values: Sequence[str]) -> str:
    rendered = ["l'asset" if item == "l'asset" else f"`{item}`" for item in values]
    if len(rendered) == 1:
        return rendered[0]
    return _join(rendered)


def _readable_field(value: str) -> str:
    labels = {
        "authorized": "l'autorizzazione",
        "configured": "la configurazione",
        "enabled": "l'abilitazione",
        "maintained": "la manutenzione",
        "monitored": "il monitoraggio",
    }
    return labels.get(value, value.replace("_", " "))


def _date(value: Any) -> str:
    text = str(value or "non disponibile")
    date = text.split("T", maxsplit=1)[0]
    parts = date.split("-")
    if len(parts) == 3 and all(part.isdigit() for part in parts):
        months = [
            "gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno",
            "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre",
        ]
        month = int(parts[1])
        if 1 <= month <= 12:
            return f"{int(parts[2])} {months[month - 1]} {parts[0]}"
    return text


def _human_scope(value: Any) -> str:
    text = _lower(_sentence_fragment(value))
    replacements = {
        "remediation": "rimozione",
        "vulnerability assessment": "valutazione delle vulnerabilità",
        "VA e penetration test": "valutazioni e test tecnici approfonditi",
        "mFA": "autenticazione a più fattori",
        "mfa": "autenticazione a più fattori",
        "selezionate in modo tri-state": "selezionate distinguendo stati noti, sconosciuti e contrastanti",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    return text


def _scope_with_article(value: Any) -> str:
    text = _human_scope(value)
    if text in SCOPE_LABELS:
        return SCOPE_LABELS[text]
    if not text or text.startswith(("il ", "lo ", "la ", "l'", "i ", "gli ", "le ")):
        return text
    articles = {
        "adeguatezza": "l'",
        "aggiornamento": "l'",
        "autenticazione": "l'",
        "cifratura": "la ",
        "completezza": "la ",
        "configurazione": "la ",
        "dispositivi": "i ",
        "giudizio": "il ",
        "monitoraggio": "il ",
        "piano": "il ",
        "presenza": "la ",
        "profondità": "la ",
        "uso": "l'",
    }
    first = text.split(maxsplit=1)[0]
    article = articles.get(first)
    return article + text if article else text


def _prepositional_scope(value: str) -> str:
    contractions = {
        "la ": "alla ",
        "l'": "all'",
        "il ": "al ",
        "lo ": "allo ",
        "i ": "ai ",
        "gli ": "agli ",
        "le ": "alle ",
    }
    for article, contraction in contractions.items():
        if value.startswith(article):
            rendered = contraction + value[len(article):]
            for source, target in (
                (", la ", ", alla "),
                (", l'", ", all'"),
                (", il ", ", al "),
                (", lo ", ", allo "),
                (", i ", ", ai "),
                (", gli ", ", agli "),
                (", le ", ", alle "),
                (" e la ", " e alla "),
                (" e l'", " e all'"),
                (" e il ", " e al "),
                (" e lo ", " e allo "),
                (" e i ", " e ai "),
                (" e gli ", " e agli "),
                (" e le ", " e alle "),
            ):
                rendered = rendered.replace(source, target)
            return rendered
    return "a " + value


def _human_action(value: Any) -> str:
    fragment = _sentence_fragment(value)
    text = _sentence(ACTION_LABELS.get(fragment, fragment))
    replacements = {
        "Remediare": "Rimuovere",
        "remediare": "rimuovere",
        "vulnerability assessment": "valutazione delle vulnerabilità",
        "patching": "aggiornamento",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    return text


def _source_label(value: Any) -> str:
    text = str(value or "").strip()
    return SOURCE_LABELS.get(text, f"dalla fonte {_value(text)}" if text else "")


def _risk_value(value: Any) -> str:
    return {
        "critical": "critico",
        "high": "alto",
        "medium": "medio",
        "low": "basso",
    }.get(str(value), _value(value))


def _value(value: Any) -> str:
    if value is None or value == "":
        return "non disponibile"
    if value is True:
        return "sì"
    if value is False:
        return "no"
    return ITALIAN_VALUES.get(str(value), str(value))


def _sentence(value: Any) -> str:
    text = str(value or "").strip()
    return text if not text or text.endswith((".", "!", "?")) else text + "."


def _sentence_fragment(value: Any) -> str:
    return str(value or "").strip().rstrip(".")


def _lower(value: str) -> str:
    return value[:1].lower() + value[1:] if value else value


def _quantity(
    value: int, singular: str, plural: str, *, feminine: bool = False
) -> str:
    if value == 0:
        article = "nessuna" if feminine else "nessun"
        return f"{article} {singular}"
    if value == 1:
        if feminine and singular[:1].lower() in "aeiou":
            return f"un'{singular}"
        article = "una" if feminine else "un"
        return f"{article} {singular}"
    return f"{value} {plural}"


def _status_reference(value: int, singular: str, plural: str) -> str:
    subject = "nessuno" if value == 0 else "uno" if value == 1 else str(value)
    return f"{subject} {singular if value < 2 else plural}"


def _non_compliant_reference(value: int, *, report_style: bool = False) -> str:
    if value == 0:
        return "nessuno risulta non soddisfatto"
    if value == 1:
        return "uno non risulta soddisfatto" if report_style else "uno non è soddisfatto"
    return f"{value} non risultano soddisfatti" if report_style else f"{value} non sono soddisfatti"


def _not_verifiable_reference(value: int) -> str:
    if value == 0:
        return "nessuno risulta non verificabile"
    if value == 1:
        return "uno non è verificabile"
    return f"{value} non sono verificabili"


def _join(values: Sequence[Any]) -> str:
    rendered = [str(value) for value in values if value is not None and str(value).strip()]
    if not rendered:
        return "nessuno"
    if len(rendered) == 1:
        return rendered[0]
    return ", ".join(rendered[:-1]) + " e " + rendered[-1]


def _unique(values: Iterable[Any]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for value in values:
        text = str(value or "").strip()
        if text and text not in seen:
            seen.add(text)
            result.append(text)
    return result


def _text(value: Any) -> str:
    if value is None or value == "":
        return "non disponibile"
    if isinstance(value, Mapping):
        return json.dumps(value, ensure_ascii=False, sort_keys=True, default=str)
    if isinstance(value, Iterable) and not isinstance(value, (str, bytes)):
        return ", ".join(_text(item) for item in value) or "nessuna"
    return str(value)


def _cell(value: Any) -> str:
    return _text(value).replace("|", "\\|").replace("\n", " ")
