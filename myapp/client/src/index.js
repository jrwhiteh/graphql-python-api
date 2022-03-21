import React from "react";

import { render } from "react-dom";

import {
  ApolloClient,
  InMemoryCache,
  ApolloProvider,
  useQuery,
  gql,
} from "@apollo/client";
import { isCompositeType } from "graphql";


const ALL_CARS = gql`
  query test {
    listVehicles {
      success
      errors
      vehicles {
        id
        model
        wheel
        created_at
      }
    }
  }
`;

const client = new ApolloClient({
  uri: "http://127.0.0.1:5000/graphql",

  cache: new InMemoryCache(),
});

function App() {
  return (
    <div>
      <h2>🚀 League</h2>
      <ListOfCars />
    </div>
  );
}

render(
  <ApolloProvider client={client}>
    <App />
  </ApolloProvider>,
  document.getElementById("root")
);



function ListOfCars() {
  const { loading, error, data } = useQuery(ALL_CARS);
  
  if (loading) return <p>Loading...</p>;
  console.log(data.listVehicles.vehicles)
  if (error) return <p>Error :(</p>;
  console.log("got past error")

  return data.listVehicles.vehicles.map(({ model, wheel }) => (
    <div key={model}>
      <p>
        Body = {model} <br/>
        Wheels = {wheel} <br/>
      </p>
    </div>
  ));
}

// client
//   .query({
//     query: gql`
//       query test {
//         listVehicles {
//           success
//           errors
//           vehicles {
//             id
//             model
//             wheel
//             created_at
//           }
//         }
//       }
//     `,
//   })
//   .then((result) => console.log(result));
