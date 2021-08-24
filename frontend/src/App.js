import { ApolloClient, ApolloProvider, InMemoryCache } from '@apollo/client'
import React from 'react'
import Projects from './Projects'

export default function App() {
	const client = new ApolloClient({
		cache: new InMemoryCache(),
	})

	return (
		<ApolloProvider client={client}>
			<Projects />
		</ApolloProvider>
	)
}
