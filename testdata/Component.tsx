// FILE: Component.tsx

import React from 'react';

interface Props {
  name?: string;
  age: number;
}

const UserInfo = ({ name, age }: Props) => {
  return (
    <div>
      <p>{name.toUpperCase()}</p>
      <p>Age: {age}</p>
    </div>
  );
};

export default UserInfo;
