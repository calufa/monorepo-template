import { MockedProvider } from '@apollo/client/testing'
import 'jest-styled-components'
import React from 'react'
import { default as TestRenderer } from 'react-test-renderer'
import Projects from './Projects'
import { GET_PROJECTS } from './queries'

const mocks = [
  {
    request: {
      query: GET_PROJECTS,
    },
    result: {
      data: {
        projects: [
          {
            name: 'project-1',
          },
        ],
      },
    },
  },
]

it('it works', async () => {
  const render = TestRenderer.create(
    <MockedProvider addTypename={false} mocks={mocks}>
      <Projects />
    </MockedProvider>
  )
  await new Promise(e => setTimeout(e, 50))
  expect(render.toJSON()).toMatchSnapshot()
})
