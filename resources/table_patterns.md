# High-Yield Table Patterns for Compact Academic Compendiums

In a 2-column layout (Legal, Letter, or A4), each column width is approximately 275 pt to 290 pt. To eliminate horizontal bleeding across columns and prevent Chromium row-height calculation bugs, tables must strictly follow these fixed 3-column and 4-column architectures.

## Pattern 1: Clinical Disorders and Genetic Pathology (3 Columns)
Use for inborn errors of metabolism, storage diseases, receptor syndromes, and enzymatic defects.

```html
<table style="width: 100%; table-layout: fixed; border-collapse: collapse; font-size: 6.95px; line-height: 1.09;">
  <colgroup>
    <col style="width: 27%">
    <col style="width: 33%">
    <col style="width: 40%">
  </colgroup>
  <thead>
    <tr>
      <th>Disorder and Genetics</th>
      <th>Enzyme Defect and Substrates</th>
      <th>Clinical Hallmarks and Diagnostics</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Tay-Sachs Disease</strong><br>AR; HEXA (15q)<br>Ashkenazi carrier 1:30</td>
      <td><strong>Deficient:</strong> Beta-Hexosaminidase A (alpha-subunit)<br><strong>Activator:</strong> GM2 Activator<br><strong>Substrate:</strong> GM2 Ganglioside</td>
      <td>Onset 3-6 mo, hyperacusis (startle reflex), cherry-red macular spot, blindness, dementia, macrocephaly. NO hepatosplenomegaly. EM shows whorled onion-skin lysosomes.</td>
    </tr>
  </tbody>
</table>
```

## Pattern 2: Comparative Physiological or Molecular Categories (3 Columns)
Use for Group I vs Group II hormones, Direct vs Indirect GH effects, Proteoglycans vs Glycoproteins, siRNA vs miRNA, and RIA vs ELISA.

```html
<table style="width: 100%; table-layout: fixed; border-collapse: collapse; font-size: 6.95px; line-height: 1.09;">
  <colgroup>
    <col style="width: 24%">
    <col style="width: 38%">
    <col style="width: 38%">
  </colgroup>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Category A (e.g. Group I / siRNA)</th>
      <th>Category B (e.g. Group II / miRNA)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Chemical Nature</strong></td>
      <td>Lipophilic; intracellular receptors.</td>
      <td>Hydrophilic; cell-surface receptors.</td>
    </tr>
  </tbody>
</table>
```

## Pattern 3: Enzyme Isoforms and Tissue Specificity (4 Columns)
Use for Phospholipases (PLA1 to PLD), PI-PLC isoforms, Thyroid deiodinases (D1 to D3), and DNA repair enzyme complexes.

```html
<table style="width: 100%; table-layout: fixed; border-collapse: collapse; font-size: 6.95px; line-height: 1.09;">
  <colgroup>
    <col style="width: 15%">
    <col style="width: 25%">
    <col style="width: 30%">
    <col style="width: 30%">
  </colgroup>
  <thead>
    <tr>
      <th>Isoform / Enzyme</th>
      <th>Tissue Distribution</th>
      <th>Activation / Coupling Mechanism</th>
      <th>Physiological Signaling Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>PLC-Beta (1-4)</strong></td>
      <td>Brain, vascular smooth muscle</td>
      <td>GPCRs via G-alpha-q/11 and G-beta-gamma</td>
      <td>Classic neuroendocrine and autonomic Ca2+/PKC responses.</td>
    </tr>
  </tbody>
</table>
```

## Pattern 4: Pharmacology and Pathway Inhibitors Matrix (3 Columns)
Use for enzyme blockers, receptor antagonists, chemotherapy agents, and targeted therapeutics.

```html
<table style="width: 100%; table-layout: fixed; border-collapse: collapse; font-size: 6.95px; line-height: 1.09;">
  <colgroup>
    <col style="width: 25%">
    <col style="width: 32%">
    <col style="width: 43%">
  </colgroup>
  <thead>
    <tr>
      <th>Target Pathway / Enzyme</th>
      <th>Pharmacological Agent</th>
      <th>Molecular Mechanism of Action and Indication</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Thyroid Peroxidase (TPO)</strong></td>
      <td><strong>Propylthiouracil (PTU)</strong></td>
      <td>Inhibits TPO iodination and coupling; blocks peripheral D1 deiodination.</td>
    </tr>
  </tbody>
</table>
```
