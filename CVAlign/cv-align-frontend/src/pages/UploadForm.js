
import React, { useState } from 'react';
import axios from 'axios';

const UploadForm = () => {
  const [cvFile, setCvFile] = useState(null);
  const [jobDesc, setJobDesc] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!cvFile || !jobDesc) return alert("All fields required");

    const formData = new FormData();
    formData.append('cv_file', cvFile); 
    formData.append('job_description', jobDesc);

try {
    setLoading(true);
    const response = await axios.post('http://127.0.0.1:8000/upload/', formData, {
    headers: { 'Content-Type': 'multipart/form-data' }
        });
    console.log("Upload successful:", response.data); 
    setResult(response.data);
    console.log("Upload result:", response.data);

} catch (error) {
    console.error("Upload failed", error.response?.data || error.message);
    alert("Error uploading file");
}
finally {
    setLoading(false);
    }
  };

  return (
    <div className="p-4 max-w-xl mx-auto bg-white rounded shadow">
      <form onSubmit={handleSubmit} className="space-y-4">
        <input type="file" onChange={e => setCvFile(e.target.files[0])} required />
        <textarea
          placeholder="Paste Job Description"
          className="w-full border p-2"
          value={jobDesc}
          onChange={e => setJobDesc(e.target.value)}
          required
        />
        <button type="submit" className="bg-blue-500 text-white px-4 py-2" disabled={loading}>
          {loading ? "Uploading..." : "Upload & Score"}
        </button>
      </form>

    {result && (
        <div className="mt-4 bg-gray-100 p-3 rounded">
        <p><strong>Score:</strong> {result.score}</p>
        {result.strengths && <p><strong>Strengths:</strong> {result.strengths}</p>}
        {result.weaknesses && <p><strong>Weaknesses:</strong> {result.weaknesses}</p>}
        {result.cloudinary_url && (
        <p><a href={result.cloudinary_url} target="_blank" rel="noreferrer">View Uploaded File</a></p>
    )}
  </div>
)}

    </div>
  );
};

export default UploadForm;
