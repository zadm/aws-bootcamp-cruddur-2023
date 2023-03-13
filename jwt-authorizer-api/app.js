const { CognitoJwtVerifier } = require("aws-jwt-verify");
const express = require("express");
const app = express();
const port = 3002;

// Create the verifier outside your route handlers,
// so the cache is persisted and can be shared amongst them.
const jwtVerifier = CognitoJwtVerifier.create({
  userPoolId: "eu-west-1_pIL9bTPxv",
  tokenUse: "access",
  clientId: "6k3b101ejkmvk1al0tqjqav1vp",
});

console.log("start application")
app.get("/auth/*", async (req, res, next) => {
  console.log("request received")
  try {
    // A valid JWT is expected in the HTTP header "authorization"
    // console.log(`"Received: ${req.header()}"`);
    console.log(req.header("authorization").split(" ")[1]);
    await jwtVerifier.verify(req.header("authorization").split(" ")[1]);
  } catch (err) {
    console.error(err);
    return res.status(403).json({ statusCode: 403, message: "Forbidden" });
  }
  res.json({ private: "only visible to users sending a valid JWT" });
});
app.get("/", async (req, res, next) => {
  console.log("hemmmmm")
});

// Hydrate the JWT verifier, then start express.
// Hydrating the verifier makes sure the JWKS is loaded into the JWT verifier,
// so it can verify JWTs immediately without any latency.
// (Alternatively, just start express, the JWKS will be downloaded when the first JWT is being verified then)
jwtVerifier
  .hydrate()
  .catch((err) => {
    console.error(`Failed to hydrate JWT verifier: ${err}`);
    process.exit(1);
  })
  .then(() =>
    app.listen(port, '0.0.0.0', () => {
      console.log(`Example app listening at http://localhost:${port}`);
    })
  );

module.exports = app;
