async function analyzeResume() {
    const resumeText = document.getElementById("resumeText").value.trim();
    const jobDescription = document.getElementById("jobDescription").value.trim();

    const resultDiv = document.getElementById("result");
    const loadingDiv = document.getElementById("loading");

    if (!resumeText || !jobDescription) {
        alert("Please enter both resume text and job description.");
        return;
    }

    resultDiv.classList.add("hidden");
    loadingDiv.classList.remove("hidden");

    try {
        const response = await fetch("/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                resume_text: resumeText,
                job_description: jobDescription
            })
        });

        if (!response.ok) {
            throw new Error("Something went wrong while analyzing the resume.");
        }

        const data = await response.json();

        document.getElementById("atsScore").innerText = data.ats_score + "%";
        document.getElementById("role").innerText = data.predicted_role;
        document.getElementById("confidence").innerText = data.confidence;
        document.getElementById("recommendation").innerText = data.recommendation;

        const matchedDiv = document.getElementById("matchedSkills");
        matchedDiv.innerHTML = "";

        if (data.matched_skills.length === 0) {
            matchedDiv.innerHTML = "<span>No matched skills found</span>";
        } else {
            data.matched_skills.forEach(skill => {
                matchedDiv.innerHTML += `<span>${skill}</span>`;
            });
        }

        const missingDiv = document.getElementById("missingSkills");
        missingDiv.innerHTML = "";

        if (data.missing_skills.length === 0) {
            missingDiv.innerHTML = "<span>No missing skills</span>";
        } else {
            data.missing_skills.forEach(skill => {
                missingDiv.innerHTML += `<span>${skill}</span>`;
            });
        }

        resultDiv.classList.remove("hidden");

    } catch (error) {
        alert(error.message);
    } finally {
        loadingDiv.classList.add("hidden");
    }
}