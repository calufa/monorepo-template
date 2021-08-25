import { ApolloClient, ApolloProvider, InMemoryCache } from '@apollo/client'
import React from 'react'
import { apiURI } from './config'
import Projects from './Projects'

export default function App() {
	const client = new ApolloClient({
		cache: new InMemoryCache(),
		uri: apiURI,
	})

	return (
		<ApolloProvider client={client}>
			<Projects />
		</ApolloProvider>
	)
}
