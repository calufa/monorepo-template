import { useQuery } from '@apollo/client'
import React from 'react'
import styled from 'styled-components'
import { GET_PROJECTS } from './queries'

const Container = styled('div')`
	background: red;
	width: 200px;
	height: 200px;
`

export default function Projects() {
	const { loading, error, data } = useQuery(GET_PROJECTS)

	if (loading) return <p>Loading...</p>
	if (error) return <p>{JSON.stringify(error)}</p>

	return (
		<Container>
			{ data.projects[0].name }
		</Container>
	)
}
