
import React from "react";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();

  const handleRoleClick = (role) => {
    
    console.log("Selected role:", role);
    navigate("/dashboard"); 
  };

  return (
    <div className="min-h-screen flex flex-col justify-center items-center bg-gray-100">
      <h1 className="text-3xl font-bold mb-6">Login As</h1>
      <div className="space-y-4">
        <button
          onClick={() => handleRoleClick("recruiter")}
          className="bg-blue-500 text-white px-6 py-2 rounded shadow"
        >
          Recruiter
        </button>
        <button
          onClick={() => handleRoleClick("manager")}
          className="bg-green-500 text-white px-6 py-2 rounded shadow"
        >
          Hiring Manager
        </button>
        <button
          onClick={() => handleRoleClick("admin")}
          className="bg-red-500 text-white px-6 py-2 rounded shadow"
        >
          Admin
        </button>
      </div>
    </div>
  );
};

export default Login;
