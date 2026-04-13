// ================= GLOBAL =================
let ACTIVE_POLICY = null;

// ================= SET POLICY =================
function setPolicy() {
  ACTIVE_POLICY = document.getElementById("active_policy").value;

  if (!ACTIVE_POLICY) {
    alert("Enter policy ID");
    return;
  }

  document.getElementById("current_policy").innerText =
    "Active Policy: " + ACTIVE_POLICY;
}

// ================= SAFE FETCH =================
async function safeFetch(url, options = {}) {
  try {
    const res = await fetch(url, options);

    let data;
    try {
      data = await res.json();
    } catch {
      const text = await res.text();
      alert("Server Error:\n" + text);
      return null;
    }

    return data;
  } catch (err) {
    alert("Network Error");
    return null;
  }
}

// ================= UPLOAD =================
async function upload() {
  const file = document.getElementById("file").files[0];

  if (!file) {
    alert("Select a file");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  const data = await safeFetch("/api/upload-policy/", {
    method: "POST",
    body: formData
  });

  if (!data) return;

  ACTIVE_POLICY = data.policy_id;

  document.getElementById("upload_result").innerText =
    "Uploaded Policy ID: " + data.policy_id;

  document.getElementById("current_policy").innerText =
    "Active Policy: " + data.policy_id;
}

// ================= COVERAGE =================
async function getCoverage() {
  if (!ACTIVE_POLICY) return alert("Set policy first");

  const data = await safeFetch(
    `/api/coverage/?policy_id=${ACTIVE_POLICY}`
  );

  if (!data) return;

  document.getElementById("coverage").innerText =
    "✅ Covered:\n- " + (data.covered?.join("\n- ") || "None") +
    "\n\n❌ Not Covered:\n- " + (data.not_covered?.join("\n- ") || "None") +
    "\n\n⚠️ Conditions:\n- " + (data.conditions?.join("\n- ") || "None");
}

// ================= ASK =================
async function ask() {
  if (!ACTIVE_POLICY) return alert("Set policy first");

  const query = document.getElementById("query").value;

  if (!query) {
    alert("Enter a question");
    return;
  }

  const data = await safeFetch("/api/ask/", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      query,
      policy_id: ACTIVE_POLICY
    })
  });

  if (!data) return;

  document.getElementById("answer").innerText = data.answer;
}

// ================= SCENARIO =================
async function simulate() {
  if (!ACTIVE_POLICY) return alert("Set policy first");

  const scenario = document.getElementById("scenario").value;

  if (!scenario) {
    alert("Enter scenario");
    return;
  }

  const data = await safeFetch("/api/simulate/", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      scenario,
      policy_id: ACTIVE_POLICY
    })
  });

  if (!data) return;

  // ✅ CORRECT TARGET
  document.getElementById("simulation").innerText =
    "Decision: " + (data.decision || "N/A") +
    "\nReason: " + (data.reason || "N/A") +
    "\nRisk: " + (data.risk_level || "N/A");
}
// ================= SCORE =================
async function score() {
  if (!ACTIVE_POLICY) return alert("Set policy first");

  const data = await safeFetch(
    `/api/score/?policy_id=${ACTIVE_POLICY}`
  );

  if (!data) return;

  document.getElementById("score").innerText =
    "Score: " + data.score +
    "\n\nSummary:\n" + data.summary +
    "\n\nPros:\n- " + (data.pros?.join("\n- ") || "None") +
    "\n\nCons:\n- " + (data.cons?.join("\n- ") || "None");
}

// ================= HIDDEN CLAUSES =================
async function getHiddenClauses() {
  if (!ACTIVE_POLICY) return alert("Set policy first");

  const data = await safeFetch(
    `/api/hidden/?policy_id=${ACTIVE_POLICY}`
  );

  if (!data) return;

  document.getElementById("hidden").innerText =
    "⚠️ Hidden Clauses:\n- " +
    (data.hidden_clauses?.join("\n- ") || "None") +
    "\n\n📊 Risk: " + (data.severity || "N/A") +
    "\n\n💡 Summary:\n" + (data.risk_summary || "N/A");
}
// ================= COMPARE PAGE =================
async function compare() {
  const p1 = document.getElementById("p1").value;
  const p2 = document.getElementById("p2").value;

  if (!p1 || !p2) {
    alert("Enter both policy IDs");
    return;
  }

  const data = await safeFetch("/api/compare/", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      policy_1: p1,
      policy_2: p2
    })
  });

  if (!data) return;

  document.getElementById("result").innerText =
    "🏆 Better Policy: " + (data.better_policy || "N/A") +
    "\n\nVerdict:\n" + (data.verdict || "N/A") +
    "\n\nDifferences:\n- " + (data.differences?.join("\n- ") || "None");
}

async function predictClaim() {
  if (!ACTIVE_POLICY) return alert("Set policy first");

  const scenario = document.getElementById("claim_scenario").value;

  const data = await safeFetch("/api/claim-predict/", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      scenario,
      policy_id: ACTIVE_POLICY
    })
  });

  if (!data) return;

  document.getElementById("claim_result").innerText =
    "📊 Approval Probability: " + data.approval_probability + "%" +
    "\n🧠 Decision: " + data.decision +
    "\n\n🔍 Extracted Features:\n" +
    JSON.stringify(data.extracted_features, null, 2) +
    "\n\n⚠️ Factors:\n- " + (data.factors?.join("\n- ") || "None") +
    "\n\n💡 Explanation:\n" + data.explanation;
}